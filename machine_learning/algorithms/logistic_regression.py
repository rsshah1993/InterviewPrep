import numpy as np


class LogisticRegression:
    def __init__(self):
        pass

    def train(self, X: np.ndarray, y: np.ndarray):
        pass

    def predict(self, X: np.ndarray):
        pass

    def _sigmoid(self, z: np.ndarray) -> np.ndarray:
        return 1 / 1 + np.exp(-z)
