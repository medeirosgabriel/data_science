# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler
import numpy as np

base = pd.read_csv('..\\Data\\credit_card_clients.csv', header = 1)
base['BILL_TOTAL'] = base['BILL_AMT1'] + base['BILL_AMT2'] + base['BILL_AMT3'] + base['BILL_AMT4'] + base['BILL_AMT5'] + base['BILL_AMT6']

x = base.iloc[:,[1,25]].values
scaler = StandardScaler()
x = scaler.fit_transform(x)

dbscan = DBSCAN(eps = 0.37, min_samples = 4)
predictions = dbscan.fit_predict(x)
uniques, qtd = np.unique(predictions, return_counts = True)

plt.scatter(x[predictions == 0, 0], x[predictions == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(x[predictions == 1, 0], x[predictions == 1, 1], s = 100, c = 'blue', label = 'Cluster 2')
plt.scatter(x[predictions == 2, 0], x[predictions == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.xlabel('Limit')
plt.ylabel('Spending')
plt.legend()