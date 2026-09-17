import sys

import pandas as pd

from src.project_name.exception import CustomException
from src.project_name.utils import load_object


class PredictPipeline:
    def __init__(self, model_path, preprocessor_path):
        self.model_path = model_path
        self.preprocessor_path = preprocessor_path

    def predict(self, features):
        try:
            model = load_object(self.model_path)
            preprocessor = load_object(self.preprocessor_path)
            transformed_features = preprocessor.transform(features)
            prediction = model.predict(transformed_features)
            return prediction

        except Exception as exc:
            raise CustomException(exc, sys) from exc


class CustomData:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    def get_data_as_dataframe(self):
        return pd.DataFrame([self.__dict__])
