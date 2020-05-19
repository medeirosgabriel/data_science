# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("..\\Data\\health_insurance_2.csv")

features = df.iloc[:,0:1].values
target = df.iloc[:,1:2].values

# Scaler is very import to SVM Algorithm
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
features = scaler.fit_transform(features)
target = scaler.fit_transform(target)

# kernel Linear
from sklearn.svm import SVR
regression = SVR(kernel='linear')
regression.fit(features, target)
score_1 = regression.score(features, target)

import matplotlib.pyplot as plt
plt.scatter(features, target)
plt.plot(features, regression.predict(features), color = 'red')
plt.title("Random Forest Regression")
plt.xlabel("Age")
plt.ylabel("Cost")

# kernel poly
from sklearn.svm import SVR
regression = SVR(kernel='poly', degree=3)
regression.fit(features, target)
score_2 = regression.score(features, target)

import matplotlib.pyplot as plt
plt.scatter(features, target)
plt.plot(features, regression.predict(features), color = 'b')
plt.title("Random Forest Regression")
plt.xlabel("Age")
plt.ylabel("Cost")

# kernel rbf

from sklearn.svm import SVR
regression = SVR(kernel='rbf')
regression.fit(features, target)
score_3 = regression.score(features, target)

import matplotlib.pyplot as plt
plt.scatter(features, target)
plt.plot(features, regression.predict(features), color = 'g')
plt.title("Random Forest Regression")
plt.xlabel("Age")
plt.ylabel("Cost")