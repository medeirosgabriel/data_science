# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

x = [20, 27, 21, 37, 46, 53, 55, 47, 52, 32, 39, 41, 39, 48, 48]  
y = [1000, 1200, 2900, 1850, 900, 950, 2000, 2100, 3000, 5900, 4100, 5100, 7000, 5000, 6500]

plt.scatter(x,y)

df = np.array([[20,1000],[27,1200],[21,2900],[37,1850],[46,900],
                 [53,950],[55,2000],[47,2100],[52,3000],[32,5900],
                 [39,4100],[41,5100],[39,7000],[48,5000],[48,6500]])

scaler = StandardScaler()
df = scaler.fit_transform(df)

kmeans = KMeans(n_clusters = 3)
kmeans.fit(df)

cent = kmeans.cluster_centers_
labels = kmeans.labels_

colors = ["g.", "r.", "b."]

for i in range(len(x)):
    plt.plot(df[i][0], df[i][1], colors[labels[i]], markersize = 15)
    
plt.scatter(cent[:,0], cent[:,1], marker = "x")