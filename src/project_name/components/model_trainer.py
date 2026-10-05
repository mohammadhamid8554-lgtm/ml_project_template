import sys
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# 🔗 CONNECTIONS
from src.project_name.exception import CustomException
from src.project_name.logger import logging
from src.project_name.utils import save_object


class ModelTrainer:
    """
    Step 3 of the ML Pipeline: Take the fully cleaned data, train the machine 
    learning model, check its accuracy, and save the winning model to the hard drive.
    """

    def __init__(self, model_path):
        # We need to know where to save the model file when we are done
        self.model_path = model_path

    def initiate_model_training(self, X_train, X_test, y_train, y_test):
        try:
            logging.info("Starting model training")
            
            # 1. Choose the algorithm (In a real project, you might test 5+ algorithms here)
            model = LinearRegression()
            
            # 2. Train the model by giving it the questions (X) and the answers (y)
            model.fit(X_train, y_train)

            # 3. Ask the trained model to predict the answers for both train and test sets
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)

            # 4. Calculate how accurate the predictions are (R2 score for regression)
            train_score = r2_score(y_train, y_train_pred)
            test_score = r2_score(y_test, y_test_pred)

            # 5. Save the trained model to the hard drive
            save_object(self.model_path, model)

            logging.info("Training complete. Train score: %.4f, Test score: %.4f", train_score, test_score)
            
            # Return the accuracy scores
            return train_score, test_score

        except Exception as exc:
            raise CustomException(exc, sys) from exc
