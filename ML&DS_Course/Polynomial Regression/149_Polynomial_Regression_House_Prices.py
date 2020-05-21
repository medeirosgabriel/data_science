# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv("..\\Data\\house_prices.csv")

features = df.iloc[:, 3:19].values
target = df.iloc[:, 2].values

from sklearn.model_selection import train_test_split
f_train, f_test, t_train, t_test = train_test_split(features, target, test_size = 0.3, random_state = 0)

from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(degree = 4)
f_train_poly = poly.fit_transform(f_train)
f_test_poly = poly.transform(f_test)

from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(f_train_poly, t_train)
score = regression.score(f_train_poly, t_train)

predictions = regression.predict(f_test_poly)

from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(t_test, predictions)