import pandas as pd
import joblib
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_PATH = BASE_DIR / "data" / "raw" / "customer_booking.csv"
OUTPUT_PATH = BASE_DIR / "outputs" / "booking_model.pkl"

# Load data
df = pd.read_csv(DATA_PATH, encoding="latin-1")

# Target
y = df["booking_complete"]

# Features
X = df.drop(columns=["booking_complete"])

# Convert categorical variables
X = pd.get_dummies(X)

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Create outputs folder if missing
OUTPUT_PATH.parent.mkdir(exist_ok=True)

# Save model
joblib.dump(model, OUTPUT_PATH)

print("Model saved to:", OUTPUT_PATH)