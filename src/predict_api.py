import joblib
import pandas as pd
from fastapi import FastAPI
from pathlib import Path
from pydantic import BaseModel

app = FastAPI()

class BookingInput(BaseModel):
    num_passengers: int
    sales_channel: str
    trip_type: str
    purchase_lead: int
    length_of_stay: int
    flight_hour: int
    flight_day: str
    route: str
    booking_origin: str
    wants_extra_baggage: int
    wants_preferred_seat: int
    wants_in_flight_meals: int
    flight_duration: float

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "outputs" / "booking_model.pkl"

model = joblib.load(MODEL_PATH)

@app.get("/")
def home():
    return {"message": "BA Booking Prediction API"}

@app.post("/predict")
def predict(data: BookingInput):

    df = pd.DataFrame([data.dict()])

    # Apply same encoding used during training
    df = pd.get_dummies(df)

    # Align with model features
    model_features = model.feature_names_in_

    df = df.reindex(columns=model_features, fill_value=0)

    prediction = model.predict(df)[0]

    return {"prediction": int(prediction)}