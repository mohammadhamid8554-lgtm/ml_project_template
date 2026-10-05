import sys  # Built-in tool to track exactly where errors happen in the system

# 🔗 CONNECTIONS: Pulling in tools from our 'src' folder (made possible by setup.py)
from src.project_name.exception import CustomException  # Connects to our custom error formatter
from src.project_name.logger import logging             # Connects to our logging system to record events
from src.project_name.pipelines.training_pipeline import TrainPipeline # Connects to the main machine learning workflow


# This ensures the code below only runs if we run main.py directly from the terminal
if __name__ == "__main__":
    # 🔗 Connection: Sending a message to logger.py
    logging.info("Project started.")

    try:
        # 🔗 Connection: Reaching into training_pipeline.py to start the model training
        pipeline = TrainPipeline()
        pipeline.run_pipeline()
        
        logging.info("Project finished successfully.")
        
    except Exception as exc:
        # 🔗 Connection: If anything breaks, hand the error to exception.py for a clean crash report
        raise CustomException(exc, sys) from exc
