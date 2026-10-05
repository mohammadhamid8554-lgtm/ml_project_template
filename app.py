import sys  # Built-in tool to interact with the system (used here for detailed error tracking)

# Importing custom tools from our 'src' folder
from src.project_name.exception import CustomException  # Handles and formats errors clearly
from src.project_name.logger import logging             # Records what happens while the app runs
from src.project_name.pipelines.training_pipeline import TrainPipeline # The blueprint for training the model


# This ensures the code below only runs if we run app.py directly
if __name__ == "__main__":
    logging.info("Application started.") # Record that we've begun

    try:
        # Attempt to create and run the training pipeline
        pipeline = TrainPipeline()
        pipeline.run_pipeline()
        
        # If it finishes without crashing, record a success message
        logging.info("Training pipeline ended successfully.")
        
    except Exception as exc:
        # If anything breaks above, catch the error (exc)
        # Pass it to our CustomException with 'sys' to find exactly which line caused the crash
        raise CustomException(exc, sys) from exc
