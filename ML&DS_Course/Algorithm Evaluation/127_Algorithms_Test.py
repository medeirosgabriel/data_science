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

from sklearn.naive_bayes import GaussianNB
classifier = GaussianNB()

from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score

results_30 = []

import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier

for i in range(30):
    kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=i) # Takes different training and test data 10 times
    results = []
    for training_index, test_index in kfold.split(features, np.zeros(shape=(features.shape[0], 1))):
        #classifier = GaussianNB()
        #classifier = DecisionTreeClassifier()
        #classifier = LogisticRegression()
        #classifier = SVC(kernel = 'rbf', random_state = 1, C = 2.0)
        #classifier = KNeighborsClassifier(n_neighbors=5, metric='minkowski', p = 2)
        #classifier = RandomForestClassifier(n_estimators=40, criterion='entropy', random_state=0)
        '''classifier = MLPClassifier(verbose = True, max_iter = 1000,
                              tol = 0.000010, solver='adam',
                              hidden_layer_sizes=(100), activation = 'relu',
                              batch_size=200, learning_rate_init=0.001)'''
        classifier.fit(features[training_index], target[training_index])
        predictions = classifier.predict(features[test_index])
        precision = accuracy_score(target[test_index], predictions)
        results.append(precision)
    results = np.asarray(results)
    mean = results.mean()
    results_30.append(mean)
results_30 = np.asarray(results_30)
for r in results_30:
    print(str(r).replace(".", ","))
    
