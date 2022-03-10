import numpy as np


class LogisticRegression:
    def __init__(self, iters: int, lr: float):
        self.iters = iters
        self.lr = lr
        self.W = None

    def _sigmoid(self, z: np.ndarray) -> np.ndarray:
        return 1 / (1 + np.exp(-z))

    def _cross_entropy(self, h: np.ndarray, y: np.ndarray) -> float:
        return (-y * np.log(h) - (1 - y) * np.log(1 - h)).mean()

    def train(self, X: np.ndarray, y: np.ndarray, verbose: bool = True) -> None:
        n, m = X.shape

        # initialize weights
        self.W = np.zeros(m)

        for i in range(self.iters):
            h = self.predict_proba(X)
            gradient = np.dot(X.T, (h - y)) / n
            self.W = self.W - self.lr * gradient

            if verbose and i % 200 == 0:
                loss = self._cross_entropy(h, y)
                print(f"Epoch {i} of {self.iters} - loss: {loss :.2f}")

    def predict_proba(self, X: np.ndarray) -> np.ndarray:
        return self._sigmoid(np.dot(X, self.W))

    def predict(self, X: np.ndarray) -> np.ndarray:
        return self.predict_proba(X).round()

    def _sigmoid(self, z: np.ndarray) -> np.ndarray:
        return 1 / (1 + np.exp(-z))


if __name__ == "__main__":
    from sklearn import datasets
    import matplotlib.pyplot as plt

    iris = datasets.load_iris()
    X = iris.data[:, :2]
    y = (iris.target != 0) * 1

    log_reg = LogisticRegression(lr=0.1, iters=10000)
    log_reg.train(X, y, verbose=True)

    preds = log_reg.predict(X)

    plt.figure(figsize=(7, 5))
    plt.scatter(X[:, 0], X[:, 1], c=preds)
    plt.show()
