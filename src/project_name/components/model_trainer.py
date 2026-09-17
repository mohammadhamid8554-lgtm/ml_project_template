import sys

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

from src.project_name.exception import CustomException
from src.project_name.logger import logging
from src.project_name.utils import save_object


class ModelTrainer:
    """Train a simple ML model and save it."""

    def __init__(self, model_path):
        self.model_path = model_path

    def initiate_model_training(self, X_train, X_test, y_train, y_test):
        try:
            model = LinearRegression()
            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            train_score = r2_score(y_train, y_train_pred)
            test_score = r2_score(y_test, y_test_pred)

            save_object(self.model_path, model)

            logging.info("Training complete. Train score: %.4f, Test score: %.4f", train_score, test_score)
            return train_score, test_score

        except Exception as exc:
            raise CustomException(exc, sys) from exc
