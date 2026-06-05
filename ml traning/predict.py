import os
import joblib

def run_local_prediction():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(current_dir, 'backend', 'models', 'xgboost_model.joblib')

    if not os.path.exists(model_path):
        model_path = os.path.join(current_dir, 'models', 'xgboost_model.joblib')

    if not os.path.exists(model_path):
        print("Error: xgboost_model.joblib not found!")
        print("Please run 'python ml_training/train_model.py' first to generate the model file.")
        return

    model = joblib.load(model_path)
    print("🧠 UPI XGBoost Model successfully loaded for local testing.\n")

    test_transactions = [
        {"case": "Small tea stall payment", "amount": 25.0},
        {"case": "Normal grocery shopping", "amount": 450.0},
        {"case": "Suspicious high-value rapid transfer", "amount": 3500.0},
        {"case": "Extreme luxury transfer", "amount": 8500.0}
    ]

    print("--- Running AI Inference Engine ---")
    for txn in test_transactions:
        features = [[txn["amount"]]]
        prediction_code = model.predict(features)[0]
        status = "BLOCKED (Potential Fraud)" if prediction_code == 1 else "✅ APPROVED (Legitimate)"
        print(f"Description : {txn['case']}")
        print(f"UPI Amount  : ₹{txn['amount']}")
        print(f"AI Decision : {status}")
        print("-" * 35)

if __name__ == "__main__":
    run_local_prediction()
