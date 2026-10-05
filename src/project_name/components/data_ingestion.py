import os
import sys
import pandas as pd
from sklearn.model_selection import train_test_split

# 🔗 CONNECTIONS: Pull in our custom error handler and logger
from src.project_name.exception import CustomException
from src.project_name.logger import logging


class DataIngestion:
    """
    Step 1 of the ML Pipeline: Load raw data from a source (like a database or CSV) 
    and split it into Training and Testing sets.
    """

    def __init__(self, config):
        # We pass in a configuration object that contains paths (where to save files)
        self.config = config

    def initiate_data_ingestion(self):
        logging.info("Starting the Data Ingestion process")
        try:
            # 1. Read the raw data. (In a real project, this could be a SQL query!)
            source_path = os.path.join("data", "raw.csv")
            df = pd.read_csv(source_path)
            logging.info(f"Successfully read the dataset from {source_path}")

            # 2. Create the folder to save the train/test files if it doesn't exist
            os.makedirs(os.path.dirname(self.config["train_data_path"]), exist_ok=True)

            # 3. Save a copy of the raw data just in case
            df.to_csv(self.config["raw_data_path"], index=False)

            # 4. Split the data (80% for training, 20% for testing)
            train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

            # 5. Save the train and test files to the hard drive
            train_df.to_csv(self.config["train_data_path"], index=False)
            test_df.to_csv(self.config["test_data_path"], index=False)

            logging.info("Data ingestion completed successfully. Train shape: %s, Test shape: %s", train_df.shape, test_df.shape)
            
            # 6. Return the paths to the new files so the next step (Transformation) can find them
            return self.config["train_data_path"], self.config["test_data_path"]

        except Exception as exc:
            # If anything fails (like a missing file), crash cleanly
            raise CustomException(exc, sys) from exc
