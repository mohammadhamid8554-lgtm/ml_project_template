import os
from dataclasses import dataclass


@dataclass
class ConfigManager:
    def __init__(self):
        self.artifacts_dir = os.path.join("artifacts")
        os.makedirs(self.artifacts_dir, exist_ok=True)

    def get_data_ingestion_config(self):
        return {
            "raw_data_path": os.path.join(self.artifacts_dir, "raw.csv"),
            "train_data_path": os.path.join(self.artifacts_dir, "train.csv"),
            "test_data_path": os.path.join(self.artifacts_dir, "test.csv"),
        }

    def get_model_path(self):
        return os.path.join(self.artifacts_dir, "model.pkl")
