# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

df = pd.read_csv('..\\Data\\credit_data.csv')
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

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()

from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score

kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=0) # Takes different training and test data 10 times
results = []

for training_index, test_index in kfold.split(features, np.zeros(shape=(features.shape[0], 1))):
    # print("Training Index:", training_index, "Test Index:", test_index)
    classifier = GaussianNB()
    classifier.fit(features[training_index], target[training_index])
    predictions = classifier.predict(features[test_index])
    precision = accuracy_score(target[test_index], predictions)
    results.append(precision)
    
results = np.asarray(results)
print(results.mean(), results.std())
