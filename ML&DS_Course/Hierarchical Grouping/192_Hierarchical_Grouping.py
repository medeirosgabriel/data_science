# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN
from sklearn import datasets
import numpy as np

x, y = datasets.make_moons(n_samples = 1500, noise = 0.09) # 1500 random data
plt.scatter(x[:, 0], x[:, 1], s = 5)

colors = np.array(['red', 'blue'])

kmeans = KMeans(n_clusters = 2)
predictions = kmeans.fit_predict(x)
plt.scatter(x[:, 0], x[:, 1], s = 5, color = colors[predictions])

hc = AgglomerativeClustering(n_clusters = 2, affinity = 'euclidean', linkage = 'ward')
predictions = hc.fit_predict(x)
plt.scatter(x[:, 0], x[:, 1], s = 5, color = colors[predictions])

dbscan = DBSCAN(eps = 0.1)
previsoes = dbscan.fit_predict(x)
plt.scatter(x[:, 0], x[:, 1], s = 5, color = colors[predictions])
