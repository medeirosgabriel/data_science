# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv("..\\Data\\health_insurance_2.csv")

features = df.iloc[:,0:1].values
target = df.iloc[:,1].values

from sklearn.linear_model import LinearRegression
regression_1 = LinearRegression()
regression_1.fit(features, target)
score_1 = regression_1.score(features, target)
result_1 = regression_1.predict([[40]])

import matplotlib.pyplot as plt
plt.scatter(features, target)
plt.plot(features, regression_1.predict(features), color = 'red')
plt.title("Linear Regression")
plt.xlabel("Age")
plt.ylabel("Cost")

# Polinomial Regression
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree = 3)
x_poly = poly.fit_transform(features)

regression_2 = LinearRegression()
regression_2.fit(x_poly, target)
score_2 = regression_2.score(x_poly, target)
result_2 = regression_2.predict(poly.transform([[40]]))


import matplotlib.pyplot as plt
plt.scatter(features, target)
plt.plot(features, regression_2.predict(poly.fit_transform(features)), color = 'b')
plt.title("Polinomial Regression")
plt.xlabel("Age")
plt.ylabel("Cost")
