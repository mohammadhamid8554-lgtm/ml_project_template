import sys

from src.project_name.exception import CustomException
from src.project_name.logger import logging
from src.project_name.pipelines.training_pipeline import TrainPipeline


if __name__ == "__main__":
    logging.info("Project started.")

    try:
        pipeline = TrainPipeline()
        pipeline.run_pipeline()
        logging.info("Project finished successfully.")
    except Exception as exc:
        raise CustomException(exc, sys) from exc
