import numpy as np


class KMeans:
    def __init__(self, n_clusters: int):
        self.n_clusters = n_clusters

    def fit(self, X: np.ndarray) -> None:
        X = np.array(X)

        # 1. initialize centroids
        self.centroids = self.init_centroids(X)

        # repeat till convergence (i.e example labels do not change):
        labels, prev_labels = np.ones(X.shape[0]), None
        while not np.all(labels == prev_labels):
            # 2. Assign all datapoints to closest centroid
            prev_labels = labels
            labels = self.predict(X)

            # 3. Calculate new centroids by taking
            # average of examples per label
            self.centroids = self.update_centroids(X, labels)

    def update_centroids(self, X: np.ndarray, labels: np.ndarray) -> np.ndarray:
        new_centroids = np.zeros((self.n_clusters, X.shape[1]))
        for k in range(self.n_clusters):
            new_centroids[k] = np.mean(X[np.where(labels == k)], axis = 0)
        return new_centroids

    def init_centroids(self, X):
        # TODO: can do something smarter like k-means ++ to initialize
        # centroids iteratively based on distance from all previous centroids
        return X[np.random.choice(X.shape[0], self.n_clusters, replace=False)]

    def predict(self, X):
        return np.apply_along_axis(self.compute_label, 1, X)

    def compute_label(self, x):
        return np.argmin(np.sqrt(np.sum((self.centroids - x)**2, axis=1)))


if __name__ == "__main__":
    from sklearn.datasets import make_blobs
    import matplotlib.pyplot as plt

    X, y = make_blobs(centers=4, n_samples=1000)

    fig = plt.figure(figsize=(8,6))
    plt.scatter(X[:,0], X[:,1], c=y)
    plt.title("Dataset with 4 clusters")
    plt.xlabel("First feature")
    plt.ylabel("Second feature")
    plt.show()

    kmeans = KMeans(n_clusters=4)
    kmeans.fit(X)

    plt.figure(figsize=(12,10))
    plt.title("Centroids")
    plt.scatter(X[:, 0], X[:, 1], marker='.', c=y)
    plt.scatter(kmeans.centroids[:, 0], kmeans.centroids[:,1], c='r')
    plt.show()
