# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

df = pd.read_csv("Data\\credit_card_clients.csv", header = 1)
df['BILL_TOTAL'] = df['BILL_AMT1'] + df['BILL_AMT2'] + df['BILL_AMT3'] + df['BILL_AMT4'] + df['BILL_AMT5'] + df['BILL_AMT6']

x = df.iloc[:,[1,25]].values
scaler = StandardScaler()
x = scaler.fit_transform(x)

wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
    
plt.plot(range(1, 11), wcss)
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')

kmeans = KMeans(n_clusters=4, random_state=0)
predictions = kmeans.fit_predict(x)

plt.scatter(x[predictions == 0, 0], x[predictions == 0, 1], s = 100, c = 'red', label = 'Cluster 1')
plt.scatter(x[predictions == 1, 0], x[predictions == 1, 1], s = 100, c = 'orange', label = 'Cluster 2')
plt.scatter(x[predictions == 2, 0], x[predictions == 2, 1], s = 100, c = 'green', label = 'Cluster 3')
plt.scatter(x[predictions == 3, 0], x[predictions == 3, 1], s = 100, c = 'blue', label = 'Cluster 4')

plt.xlabel("Limit")
plt.ylabel("Spending")
plt.legend()

clients_list = np.column_stack((df, predictions))
clients_list = clients_list[clients_list[:,26].argsort()] # Sorts based on line 26 attribute
