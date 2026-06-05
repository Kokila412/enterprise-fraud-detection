import os
import pandas as pd
import numpy as np
import xgboost as xgb
import joblib
from sklearn.model_selection import train_test_split

print("Step 1: Generating synchronized 2-Feature data matrix (Amount, Risk)...")
np.random.seed(42)
num_samples = 5000

# Feature 1: Numerical Amount
amounts = np.random.exponential(scale=200, size=num_samples)
# Feature 2: Calculated Structural Risk Scores (0.0 to 1.5)
risk_scores = np.random.uniform(0.0, 1.2, size=num_samples)

# Logical rules linking features to the target classification state
is_fraud = np.zeros(num_samples)
for i in range(num_samples):
    if risk_scores[i] >= 0.7 or (amounts[i] > 2000 and risk_scores[i] > 0.4):
        is_fraud[i] = 1
    else:
        is_fraud[i] = np.random.choice([0, 1], p=[0.99, 0.01])

df = pd.DataFrame({"amount": amounts, "risk_score": risk_scores, "is_fraud": is_fraud})

X = df[['amount', 'risk_score']]
y = df['is_fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Step 2: Training updated XGBoost Classifier pipeline...")
model = xgb.XGBClassifier(scale_pos_weight=5, random_state=42)
model.fit(X_train, y_train)

# Direct output serialization path mapping
output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'backend', 'models'))
os.makedirs(output_dir, exist_ok=True)
joblib.dump(model, os.path.join(output_dir, 'xgboost_model.joblib'))
print("Success! Clean binary model compiled and synchronized without transaction ID parameters.")