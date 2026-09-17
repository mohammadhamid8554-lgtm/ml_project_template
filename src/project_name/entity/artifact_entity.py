from dataclasses import dataclass


@dataclass
class ModelTrainerArtifact:
    model_path: str
    train_score: float
    test_score: float
