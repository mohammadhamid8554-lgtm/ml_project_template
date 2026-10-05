import sys
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# 🔗 CONNECTIONS: Error handler, logger, and our 'save_object' utility
from src.project_name.exception import CustomException
from src.project_name.logger import logging
from src.project_name.utils import save_object


class DataTransformation:
    """
    Step 2 of the ML Pipeline: Clean the data, handle missing values, 
    scale numbers, and convert text into numbers so the model can read it.
    """

    def get_data_transformer_object(self):
        """Creates the 'recipe' for how to transform the data."""
        try:
            # 1. Define which columns are numbers and which are text/categories
            numeric_features = ["num_feature_1", "num_feature_2"]
            categorical_features = ["cat_feature_1", "cat_feature_2"]

            # 2. Recipe for numbers: fill missing values with the median, then scale them
            numeric_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler()),
                ]
            )

            # 3. Recipe for text: fill missing values with the most frequent, then turn into One-Hot numbers
            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("onehot", OneHotEncoder(handle_unknown="ignore")),
                ]
            )

            # 4. Combine both recipes into one master preprocessor
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
        """Applies the transformation recipe to the actual data."""
        try:
            # 1. Load the train/test files created by the Ingestion step
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            # 2. Separate the "answers" (target column) from the "questions" (features)
            target_column = "target"
            X_train = train_df.drop(columns=[target_column])
            y_train = train_df[target_column]
            X_test = test_df.drop(columns=[target_column])
            y_test = test_df[target_column]

            # 3. Get the transformation recipe and apply it to the features
            preprocessor = self.get_data_transformer_object()
            
            # fit_transform on training data (learns the patterns and applies them)
            X_train_processed = preprocessor.fit_transform(X_train)
            
            # just transform on testing data (applies the learned patterns)
            X_test_processed = preprocessor.transform(X_test)

            # 4. Save the transformation recipe to the hard drive so we can use it on new user data later
            save_object(preprocessor_path, preprocessor)

            logging.info("Preprocessing completed successfully.")
            return X_train_processed, X_test_processed, y_train, y_test

        except Exception as exc:
            raise CustomException(exc, sys) from exc
