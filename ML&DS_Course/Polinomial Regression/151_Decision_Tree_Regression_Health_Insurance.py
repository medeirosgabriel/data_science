# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("..\\Data\\health_insurance_2.csv")

features = df.iloc[:,0:1].values
target = df.iloc[:,1].values

from sklearn.tree import DecisionTreeRegressor
regression = DecisionTreeRegressor()
regression.fit(features, target)
score = regression.score(features, target)

import matplotlib.pyplot as plt
plt.scatter(features, target)
plt.plot(features, regression.predict(features), color = 'red')
plt.title("Tree Regression")
plt.xlabel("Age")
plt.ylabel("Cost")


import numpy as np
f_test = np.arange(min(features), max(features), 0.1)
f_test = f_test.reshape(-1, 1)
plt.scatter(features, target)
plt.plot(f_test, regression.predict(f_test), color = 'red')
plt.title("Tree Regression")
plt.xlabel("Age")
plt.ylabel("Cost")

result_1 = regression.predict([[40]])