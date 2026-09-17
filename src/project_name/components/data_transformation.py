import sys

import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from src.project_name.exception import CustomException
from src.project_name.logger import logging
from src.project_name.utils import save_object


class DataTransformation:
    """Create preprocessing steps for numeric and categorical data."""

    def get_data_transformer_object(self):
        try:
            numeric_features = ["num_feature_1", "num_feature_2"]
            categorical_features = ["cat_feature_1", "cat_feature_2"]

            numeric_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler()),
                ]
            )

            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("onehot", OneHotEncoder(handle_unknown="ignore")),
                ]
            )

            processor = ColumnTransformer(
                transformers=[
                    ("numeric", numeric_pipeline, numeric_features),
                    ("categorical", categorical_pipeline, categorical_features),
                ]
            )

            return processor

        except Exception as exc:
            raise CustomException(exc, sys) from exc

    def initiate_data_transformation(self, train_path, test_path, preprocessor_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            target_column = "target"
            X_train = train_df.drop(columns=[target_column])
            y_train = train_df[target_column]
            X_test = test_df.drop(columns=[target_column])
            y_test = test_df[target_column]

            preprocessor = self.get_data_transformer_object()
            X_train_processed = preprocessor.fit_transform(X_train)
            X_test_processed = preprocessor.transform(X_test)

            save_object(preprocessor_path, preprocessor)

            logging.info("Preprocessing completed successfully.")
            return X_train_processed, X_test_processed, y_train, y_test

        except Exception as exc:
            raise CustomException(exc, sys) from exc
