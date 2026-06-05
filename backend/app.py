import os
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS
from pydantic import ValidationError
from schemas import TransactionInput

app = Flask(__name__)
CORS(app)

model = None
base_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(base_dir, 'models', 'xgboost_model.joblib')

if os.path.exists(model_path):
    model = joblib.load(model_path)
    print("Advanced UPI Security Model Loaded Successfully.")
else:
    print("Warning: Model file not found. Run training script first.")

HISTORICAL_LEDGER = {
    "fresh_scammer@okaxis": {
        "is_new_upi_id": True,
        "is_new_bank_account": True,
        "had_recent_split_transactions": True,
        "clears_balance_to_zero": True
    },
    "mule_node@oksbi": {
        "is_new_upi_id": False,
        "is_new_bank_account": True,
        "had_recent_split_transactions": True,
        "clears_balance_to_zero": True
    },
    "trusted_merchant@okhdfc": {
        "is_new_upi_id": False,
        "is_new_bank_account": False,
        "had_recent_split_transactions": False,
        "clears_balance_to_zero": False
    }
}

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"status": "error", "message": "ML Model not initialized."}), 503

    try:
        raw_payload = request.get_json()
        validated_data = TransactionInput(**raw_payload)
        
        amount = validated_data.amount
        receiver = validated_data.receiver_upi_id.lower()
        
        risk_score = 0.0
        flagged_factors = []
        
        suspicious_keywords = ["verification", "reward", "customer_care", "helpline", "freebie"]
        if any(keyword in receiver for keyword in suspicious_keywords):
            risk_score += 0.4
            flagged_factors.append("Deceptive/Spoofed VPA Keywords Detected")
            
        receiver_history = HISTORICAL_LEDGER.get(receiver, {
            "is_new_upi_id": "new" in receiver or "fresh" in receiver,
            "is_new_bank_account": "new" in receiver or "mule" in receiver,
            "had_recent_split_transactions": "split" in receiver,
            "clears_balance_to_zero": "mule" in receiver
        })
        
        if receiver_history["is_new_upi_id"]:
            risk_score += 0.3
            flagged_factors.append("Newly Activated UPI Handle (Zero Reputation)")
            
        if receiver_history["is_new_bank_account"]:
            risk_score += 0.4
            flagged_factors.append("Freshly Opened Bank Account Node")
            
        if receiver_history["had_recent_split_transactions"]:
            risk_score += 0.5
            flagged_factors.append("Historical High-Velocity Split-Fund Behavior (Layering Network)")
            
        if receiver_history["clears_balance_to_zero"]:
            risk_score += 0.4
            flagged_factors.append("Mule Account Profile Signature (Rapid Balance Drainage Target)")

        features = [[amount, risk_score]]
        prediction_code = model.predict(features)[0]
        
        if receiver_history["is_new_upi_id"] and receiver_history["is_new_bank_account"]:
            prediction_code = 1

        if prediction_code == 1:
            return jsonify({
                "status": "success",
                "prediction": "Fraudulent Activity Blocked",
                "action": "BLOCKED",
                "factors": flagged_factors if flagged_factors else ["Anomalous Transaction Volume"]
            }), 200
        else:
            return jsonify({
                "status": "success",
                "prediction": "Legitimate Transaction",
                "action": "APPROVED",
                "explanation": "Passed all structural age and ledger verifications."
            }), 200

    except ValidationError as e:
        return jsonify({"status": "error", "message": "Schema Validation Failed.", "details": e.errors()}), 400
    except Exception as e:
        return jsonify({"status": "error", "message": f"Runtime Engine Fault: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)