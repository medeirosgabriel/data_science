# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets.samples_generator import make_blobs # Generate aleatory test data for Kmeans

x, y = make_blobs(n_samples=200, centers = 3)
plt.scatter(x[:,0], x[:,1])

kmeans = KMeans(n_clusters = 3)
kmeans.fit(x)

predictions = kmeans.predict(x)
plt.scatter(x[:,0], x[:,1], c=predictions) # c == color