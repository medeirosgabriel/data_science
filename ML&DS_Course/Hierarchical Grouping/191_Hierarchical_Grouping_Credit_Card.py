# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
from sklearn.preprocessing import StandardScaler
import numpy as np

base = pd.read_csv('..\\Data\\credit_card_clients.csv', header = 1)
base['BILL_TOTAL'] = base['BILL_AMT1'] + base['BILL_AMT2'] + base['BILL_AMT3'] + base['BILL_AMT4'] + base['BILL_AMT5'] + base['BILL_AMT6']

x = base.iloc[:,[1,25]].values
scaler = StandardScaler()
x = scaler.fit_transform(x)

dendrogram = dendrogram(linkage(x, method = 'ward'))

hc = AgglomerativeClustering(n_clusters = 3, affinity = 'euclidean', linkage = 'ward')
predictions = hc.fit_predict(x)

plt.scatter(x[predictions == 0, 0], x[predictions == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(x[predictions == 1, 0], x[predictions == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(x[predictions == 2, 0], x[predictions == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.xlabel('Limit')
plt.ylabel('Spending')
plt.legend()