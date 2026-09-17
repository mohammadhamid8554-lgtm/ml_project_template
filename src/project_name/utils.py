import os
import pickle
import sys

from src.project_name.exception import CustomException


def save_object(file_path, object_to_save):
    """Save any Python object as a pickle file."""
    try:
        directory = os.path.dirname(file_path)
        if directory:
            os.makedirs(directory, exist_ok=True)

        with open(file_path, "wb") as file_obj:
            pickle.dump(object_to_save, file_obj)

    except Exception as exc:
        raise CustomException(exc, sys) from exc


def load_object(file_path):
    """Load a pickle file back into memory."""
    try:
        with open(file_path, "rb") as file_obj:
            return pickle.load(file_obj)
    except Exception as exc:
        raise CustomException(exc, sys) from exc
