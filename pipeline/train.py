from prefect import task, flow
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import mlflow
import mlflow.sklearn
import pandas as pd
from sklearn.metrics import mean_squared_error


@task
def train_model(df: pd.DataFrame):
    # MLflow Setting
    mlflow.set_tracking_uri("http://127.0.0.1:5000")
    mlflow.set_experiment("melbourne-housing-price")
    X = df.drop("Price", axis=1)
    y = df["Price"]
    
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    with mlflow.start_run():
        model = LinearRegression()
        model.fit(X_train, y_train)

        predictions = model.predict(X_val)
        mse = mean_squared_error(y_val, predictions)

        mlflow.log_param("model_type", "LinearRegression")
        mlflow.log_metric("mse", mse)
        mlflow.sklearn.log_model(model, "model")

    return mse
