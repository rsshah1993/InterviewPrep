import numpy as np
from sklearn.utils import as_float_array


class LinearRegression:
    def __init__(self, lr: float = 0.001, iters: int = 1000):
        self.lr = lr
        self.iters = iters
        self.W = None
        self.b = None

    def train(self, X: np.ndarray, y: np.ndarray) -> None:
        m, n = X.shape
        self.W = np.zeros(n)
        self.b = 0

        for i in range(self.iters):
            preds = self.predict(X)
            error = -2 * (preds - y)/m
            self.W = self.W - self.lr/m * np.dot(X.T, error)
            self.b = self.b - self.lr * np.sum(error)

            if i % 20 == 0:
                mse = self._mse(y, preds)
                print(f"On epoch {i} of {self.iters} with error: {mse}")

    def predict(self, X: np.ndarray) -> np.ndarray:
        return np.dot(X, self.W) + self.b

    def _mse(self, y: np.ndarray, y_hat: np.ndarray) -> np.ndarray:
        return np.mean(np.sqrt((y - y_hat) ** 2))


if __name__ == "__main__":
    from sklearn.datasets import fetch_california_housing
    housing = fetch_california_housing()
    X, y = housing["data"], housing["target"]
    print(y[:5])
    reg = LinearRegression(0.01, 500)
    reg.train(X, y)

    # preds = reg.predict(X)
