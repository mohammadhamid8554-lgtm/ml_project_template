import os
import pickle  # A tool to save Python objects (like trained models) into files
import sys

# 🔗 CONNECTIONS: Pulls in our custom error formatter so if saving/loading fails, it crashes cleanly.
from src.project_name.exception import CustomException


def save_object(file_path, object_to_save):
    """
    Save any Python object (usually a trained Machine Learning model or a scaler) 
    as a physical file on your hard drive so you can use it later.
    """
    try:
        # Create the folder for the file if it doesn't already exist
        directory = os.path.dirname(file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)

        # Open the file in "wb" (write binary) mode and save the object inside it
        with open(file_path, "wb") as file_obj:
            pickle.dump(object_to_save, file_obj)

    except Exception as exc:
        raise CustomException(exc, sys) from exc


def load_object(file_path):
    """
    Load a previously saved Python object (like a trained model) from your hard drive 
    back into memory so you can use it to make predictions.
    """
    try:
        # Open the file in "rb" (read binary) mode and load the object
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as exc:
        raise CustomException(exc, sys) from exc
