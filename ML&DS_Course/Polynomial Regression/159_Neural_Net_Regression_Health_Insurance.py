# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("..\\Data\\health_insurance_2.csv")

features = df.iloc[:,0:1].values
target = df.iloc[:,1:2].values

from sklearn.preprocessing import StandardScaler
scaler_x = StandardScaler()
features = scaler_x.fit_transform(features)
scaler_y = StandardScaler()
target = scaler_y.fit_transform(target)

from sklearn.neural_network import MLPRegressor
regression = MLPRegressor()
regression.fit(features, target)
score_1 = regression.score(features, target)

import matplotlib.pyplot as plt
plt.scatter(features, target)
plt.plot(features, regression.predict(features), color = 'red')
plt.title("Neural Net Regression")
plt.xlabel("Age")
plt.ylabel("Cost")

# scaler.inverse_transform -> Back to real scale
prediction = scaler_y.inverse_transform(regression.predict(scaler_x.fit_transform([[40]])))