import sys

from src.project_name.components.data_ingestion import DataIngestion
from src.project_name.components.data_transformation import DataTransformation
from src.project_name.components.model_trainer import ModelTrainer
from src.project_name.config.configuration import ConfigManager
from src.project_name.exception import CustomException
from src.project_name.logger import logging


class TrainPipeline:
    def __init__(self):
        self.config = ConfigManager()

    def run_pipeline(self):
        try:
            ingestion_config = self.config.get_data_ingestion_config()
            train_path, test_path = DataIngestion(ingestion_config).initiate_data_ingestion()

            preprocessor_path = self.config.get_model_path().replace("model.pkl", "preprocessor.pkl")
            X_train, X_test, y_train, y_test = DataTransformation().initiate_data_transformation(
                train_path,
                test_path,
                preprocessor_path,
            )

            model_trainer = ModelTrainer(self.config.get_model_path())
            model_trainer.initiate_model_training(X_train, X_test, y_train, y_test)

            logging.info("Training pipeline completed successfully.")
            return train_path, test_path

        except Exception as exc:
            raise CustomException(exc, sys) from exc
