# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv('Data\\credit_data.csv')
df.loc[df.age < 0, 'age'] = 40.92 # Mean

features = df.iloc[:, 1:4].values
target = df.iloc[:,4].values

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values = 'NaN', strategy='mean', axis=0)
imputer = imputer.fit(features[:, 1:4])
features[:, 1:4] = imputer.transform(features[:, 1:4])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
features = scaler.fit_transform(features)

from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

SVMclassifier = SVC(kernel = 'rbf', C = 2.0, probability=True)
SVMclassifier.fit(features, target)

RandomForestclassifier = RandomForestClassifier(n_estimators = 40, criterion = 'entropy')
RandomForestclassifier.fit(features, target)

MLPclassifier = MLPClassifier(verbose = True, max_iter = 1000,
                                 tol = 0.000010, solver = 'adam',
                                 hidden_layer_sizes=(100), activation = 'relu',
                                 batch_size = 200, learning_rate_init = 0.001)
MLPclassifier.fit(features, target)

import pickle
pickle.dump(SVMclassifier, open('Models/svm.sav', 'wb')) # wb -> Save to disk 
pickle.dump(RandomForestclassifier, open('Models/random_forest.sav', 'wb'))
pickle.dump(MLPclassifier, open('Models/mlp.sav', 'wb'))
