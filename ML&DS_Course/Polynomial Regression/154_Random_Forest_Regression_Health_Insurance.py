# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("..\\Data\\health_insurance_2.csv")

features = df.iloc[:,0:1].values
target = df.iloc[:,1].values

from sklearn.ensemble import RandomForestRegressor
regression = RandomForestRegressor(n_estimators=10)
regression.fit(features, target)
score = regression.score(features, target)

import matplotlib.pyplot as plt
import numpy as np
f_test = np.arange(min(features), max(features), 0.1)
f_test = f_test.reshape(-1, 1)
plt.scatter(features, target)
plt.plot(f_test, regression.predict(f_test), color = 'red')
plt.title("Random Forest Regression")
plt.xlabel("Age")
plt.ylabel("Cost")

