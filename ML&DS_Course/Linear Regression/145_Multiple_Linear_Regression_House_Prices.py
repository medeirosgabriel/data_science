# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv("Data\\house_prices.csv")

features = df.iloc[:, 3:19].values
target = df.iloc[:, 2].values

from sklearn.model_selection import train_test_split
f_train, f_test, t_train, t_test = train_test_split(features, target, test_size = 0.3, random_state = 0)

from sklearn.linear_model import LinearRegression
regression = LinearRegression()
regression.fit(f_train, t_train)
score = regression.score(f_train, t_train)

predictions = regression.predict(f_test)
from sklearn.metrics import mean_absolute_error, mean_squared_error

err1 = mean_absolute_error(t_test, predictions)
err2 = mean_squared_error(t_test, predictions)

print(regression.intercept_)
print(regression.coef_, len(regression.coef_))
