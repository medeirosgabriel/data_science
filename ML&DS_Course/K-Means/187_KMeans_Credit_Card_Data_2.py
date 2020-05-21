# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import numpy as np

df = pd.read_csv("Data\\credit_card_clients.csv", header = 1)
df['BILL_TOTAL'] = df['BILL_AMT1'] + df['BILL_AMT2'] + df['BILL_AMT3'] + df['BILL_AMT4'] + df['BILL_AMT5'] + df['BILL_AMT6']

x = df.iloc[:,[1,2,3,4,5,25]].values
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

clients_list = np.column_stack((df, predictions))
clients_list = clients_list[clients_list[:,26].argsort()] # Sorts based on line 26 attribute