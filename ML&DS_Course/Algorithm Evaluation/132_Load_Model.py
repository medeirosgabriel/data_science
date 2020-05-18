# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import Imputer
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('Data\\credit_data.csv')
df.loc[df.age < 0, 'age'] = 40.92 # Mean

features = df.iloc[:, 1:4].values
target = df.iloc[:,4].values

imputer = Imputer(missing_values = 'NaN', strategy='mean', axis=0)
imputer = imputer.fit(features[:, 1:4])
features[:, 1:4] = imputer.transform(features[:, 1:4])

scaler = StandardScaler()
features = scaler.fit_transform(features)

svm = pickle.load(open('Models/svm.sav', 'rb'))
rf = pickle.load(open('Models/random_forest.sav', 'rb'))
mlp = pickle.load(open('Models/mlp.sav', 'rb'))

svm_result = svm.score(features, target)
rf_result = rf.score(features, target)
mlp_result = mlp.score(features, target)

new_register = [[50000, 40, 5000]]
new_register = np.asarray(new_register)
new_register = new_register.reshape(-1,1) # -1 -> Doesn't change
new_register = scaler.fit_transform(new_register)
new_register = new_register.reshape(-1,3)

svm_result2 = svm.predict(new_register)
rf_result2 = rf.predict(new_register)
mlp_result2 = mlp.predict(new_register)