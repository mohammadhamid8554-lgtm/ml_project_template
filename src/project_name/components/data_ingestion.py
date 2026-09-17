import os
import sys

import pandas as pd
from sklearn.model_selection import train_test_split

from src.project_name.exception import CustomException
from src.project_name.logger import logging


class DataIngestion:
    """Load raw data and split it into train/test sets."""

    def __init__(self, config):
        self.config = config

    def initiate_data_ingestion(self):
        try:
            source_path = os.path.join("data", "raw.csv")
            df = pd.read_csv(source_path)

            os.makedirs(os.path.dirname(self.config["train_data_path"]), exist_ok=True)

            df.to_csv(self.config["raw_data_path"], index=False)
            train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

            train_df.to_csv(self.config["train_data_path"], index=False)
            test_df.to_csv(self.config["test_data_path"], index=False)

            logging.info("Data ingestion completed. Train shape: %s, Test shape: %s", train_df.shape, test_df.shape)
            return self.config["train_data_path"], self.config["test_data_path"]

        except Exception as exc:
            raise CustomException(exc, sys) from exc
