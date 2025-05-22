import os
from pipeline.ingest import ingest_flow
from pipeline.preprocess import preprocess_flow
from pipeline.train import train_model

if __name__ == "__main__":
    raw_df = ingest_flow()
    clean_df = preprocess_flow(raw_df)
    mse = train_model(clean_df)
    print(f"✅ Training complete. MSE: {mse}")
