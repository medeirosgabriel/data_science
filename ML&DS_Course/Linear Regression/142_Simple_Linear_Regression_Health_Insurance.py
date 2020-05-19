# -*- coding: utf-8 -*-

import pandas

df = pandas.read_csv("..\\Data\\health_insurance.csv")

features = df.iloc[:, 0].values
target = df.iloc[:, 1].values

import numpy as np

corr = np.corrcoef(features, target)

features = features.reshape(-1,1)

from sklearn.linear_model import LinearRegression
regression= LinearRegression()
regression.fit(features, target)

print(regression.intercept_, regression.coef_)

import matplotlib.pyplot as plt

plt.scatter(features, target)
plt.plot(features, regression.predict(features), color='red')
plt.title("Simple Linear Regression")
plt.xlabel("Age")
plt.ylabel("Cost")

prediction_1 = regression.predict([[40]])
previcion_2 = regression.intercept_ + regression.coef_*40

score = regression.score(features, target)

from yellowbrick.regressor import ResidualsPlot
visualizer = ResidualsPlot(regression)
visualizer.fit(features, target)
visualizer.poof()