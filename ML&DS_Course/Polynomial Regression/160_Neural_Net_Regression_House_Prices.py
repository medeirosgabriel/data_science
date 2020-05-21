# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("..\\Data\\house_prices.csv")

features = df.iloc[:,3:19].values
target = df.iloc[:,2:3].values

# Scaler is very important to SVM Algorithm
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
features = scaler.fit_transform(features)
target = scaler.fit_transform(target)


from sklearn.model_selection import train_test_split
f_train, f_test, t_train, t_test = train_test_split(features, target, test_size = 0.3, random_state = 0)

from sklearn.neural_network import MLPRegressor
regression = MLPRegressor(hidden_layer_sizes=(9,9))
regression.fit(features, target)
score_1 = regression.score(f_train, t_train)

predictions = regression.predict(f_test)

score_2 = regression.score(f_test, t_test)

from sklearn.metrics import mean_absolute_error
mae_1 = mean_absolute_error(t_test, predictions)

t_test = scaler.inverse_transform(t_test)
predictions = scaler.inverse_transform(predictions)
mae_2 = mean_absolute_error(t_test, predictions)


