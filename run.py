from pipeline.ingest import ingest_flow
from pipeline.preprocess import preprocess_flow

if __name__ == "__main__":
    raw_df = ingest_flow()
    clean_df = preprocess_flow(raw_df)
    
    print(clean_df.head())
