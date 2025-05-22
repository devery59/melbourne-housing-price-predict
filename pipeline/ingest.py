from prefect import task, flow
import pandas as pd

@task
def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    return df

@flow
def ingest_flow(data_path: str = "data/melb_housing.csv") -> pd.DataFrame:
    df = load_data(data_path)
    return df
