from prefect import task, flow
import pandas as pd

@task
def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    
    # ✅ Use only necessary columns
    selected_cols = [
        'Rooms', 'Distance', 'Landsize', 'BuildingArea',
        'YearBuilt', 'Bathroom', 'Car', 'Price'
    ]
    df = df[selected_cols]

    # ✅ Remove missing values
    df = df.dropna()

    # ✅ Remove outliers (simple example)
    df = df[df['Price'] < 3_000_000]
    
    return df

@flow
def preprocess_flow(df: pd.DataFrame) -> pd.DataFrame:
    return preprocess_data(df)
