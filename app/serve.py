from fastapi import FastAPI
from pydantic import BaseModel
import mlflow.sklearn
import pandas as pd
import logging

# Logging Setting
logging.basicConfig(level=logging.INFO)

app = FastAPI()

# Load Model   
model = mlflow.sklearn.load_model("mlruns/1/5d9a1be412e24941992658a03f8e5fd2/artifacts/model")

# Features List (Check Accuracy)
FEATURES = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt', 'Bathroom', 'Car']

# Input Data Schema (If you only receive 5, the rest needs to be set to a default value)
class HousingData(BaseModel):
    rooms: float
    distance: float
    landsize: float
    building_area: float
    year_built: float
    bathroom: float = 1  
    car: float = 1       

@app.post("/predict")
def predict(data: HousingData):
    try:
        # Construct the input as a DataFrame matching the model
        input_df = pd.DataFrame([{
            "Rooms": data.rooms,
            "Distance": data.distance,
            "Landsize": data.landsize,
            "BuildingArea": data.building_area,
            "YearBuilt": data.year_built,
            "Bathroom": data.bathroom,
            "Car": data.car
        }])

        # Match the column order
        input_df = input_df[FEATURES]

        # Prediction
        prediction = model.predict(input_df)[0]
        return {"prediction": prediction}

    except Exception as e:
        logging.exception("Error during prediction")
        return {"error": str(e)}
