# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv("..//Data//credit_data.csv")
df = df.dropna()

from pyod.models.knn import KNN
detector = KNN()
detector.fit(df.iloc[:,1:4])

predictions = detector.labels_ # 0 == It's not an outlier 1 == It's an outlier
predictions_confiance = detector.decision_scores_ # The higher, the greater the chance of being a discrepant

outliers = []
for i in range(len(predictions)):
    #print(previsoes[i])
    if predictions[i] == 1:
        outliers.append(i)
        
lista_outliers = df.iloc[outliers, :]
    