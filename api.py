from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import numpy as np
from tensorflow.keras.models import load_model
from sklearn.preprocessing import MinMaxScaler
import tensorflow as tf
import joblib
from datetime import datetime

# Define the custom MSE function
def mse(y_true, y_pred):
    return tf.keras.losses.MeanSquaredError()(y_true, y_pred)

# Initialize the FastAPI app
app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Load the trained model
model_path = "./model.h5"  # Adjust the path if necessary
model = load_model(model_path, custom_objects={"mse": mse})

# Recompile the model
model.compile(optimizer='adam', loss=mse, metrics=['mse'])

# Load the saved scalers
scaler_X = joblib.load('scaler_X.pkl')
scaler_y = joblib.load('scaler_y.pkl')

# Define the request body schema
class PredictionRequest(BaseModel):
    store: int
    date: str
    promo: int

# API Endpoint: Health check
@app.get("/")
def read_root():
    return {"message": "Rossmann Sales Prediction API is running!"}

# API Endpoint: Predict
@app.post("/predict/")
def predict(request: PredictionRequest):
    try:
        # Extract input data
        store = request.store
        date = datetime.strptime(request.date, "%Y-%m-%d")
        promo = request.promo

        # Create feature vector with 6 features (matching the scaler)
        input_data = np.array([[
            store,  # Store
            date.weekday(),  # DayOfWeek
            promo,  # Promo
            0,  # StateHoliday (default: 0)
            0,  # SchoolHoliday (default: 0)
            2000,  # CompetitionDistance (default: 2000)
        ]])

        # Scale the input data
        input_data_scaled = scaler_X.transform(input_data)

        # Reshape the input data to (1, 1, 6) for LSTM
        input_data_scaled = input_data_scaled.reshape(1, 1, -1)

        # Make the prediction
        scaled_prediction = model.predict(input_data_scaled)

        # Inverse transform the prediction
        original_prediction = scaler_y.inverse_transform(scaled_prediction)

        # Return the prediction
        return {"prediction": float(original_prediction[0][0])}

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))