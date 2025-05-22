from prefect import task
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import mlflow
import mlflow.sklearn
from mlflow.tracking import MlflowClient
import pandas as pd
import numpy as np


@task
def train_model(df: pd.DataFrame) -> float:
    # Set MLflow settings
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment("melbourne-housing-price")

    # Split features and target
    X = df.drop("Price", axis=1)
    y = df["Price"]

    # Train/validation split
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    with mlflow.start_run() as run:
        # Train model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Predict & calculate metrics
        y_pred = model.predict(X_val)
        mse = mean_squared_error(y_val, y_pred)
        rmse = np.sqrt(mse)
        r2 = r2_score(y_val, y_pred)

        # Log params and metrics
        mlflow.log_param("model_type", "LinearRegression")
        mlflow.log_metric("mse", mse)
        mlflow.log_metric("rmse", rmse)
        mlflow.log_metric("r2", r2)

        # Log model
        mlflow.sklearn.log_model(model, "model")

        # Register model
        model_uri = f"runs:/{run.info.run_id}/model"
        model_name = "MelbourneHousingModel"

        client = MlflowClient()
        try:
            client.get_registered_model(model_name)
        except:
            client.create_registered_model(model_name)

        client.create_model_version(
            name=model_name,
            source=model_uri,
            run_id=run.info.run_id
        )

        print(f"✅ Model registered as '{model_name}' with run ID: {run.info.run_id}")
        return mse
