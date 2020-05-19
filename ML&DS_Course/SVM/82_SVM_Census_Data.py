# -*- coding: utf-8 -*-

import pandas as pd
pd.set_option('display.max_columns', None) # See all dataframe columns

df = pd.read_csv('..\\Data\\census_data.csv')

features = df.iloc[:,0:14].values
target = df.iloc[:,14].values

from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:, 1] = labelencoder.fit_transform(features[:,1])
features[:, 3] = labelencoder.fit_transform(features[:,3])
features[:, 5] = labelencoder.fit_transform(features[:,5])
features[:, 6] = labelencoder.fit_transform(features[:,6])
features[:, 7] = labelencoder.fit_transform(features[:,7])
features[:, 8] = labelencoder.fit_transform(features[:,8])
features[:, 9] = labelencoder.fit_transform(features[:,9])
features[:, 13] = labelencoder.fit_transform(features[:,13])

from sklearn.preprocessing import OneHotEncoder # Generate binary vectors for each integer value.
onehotencoder = OneHotEncoder(categorical_features=[1,3,5,6,7,8,9,13])
features = onehotencoder.fit_transform(features).toarray()

target = labelencoder.fit_transform(target)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
features = scaler.fit_transform(features)

from sklearn.model_selection import train_test_split
f_train, f_test, t_train, t_test = train_test_split(features, target, test_size = 0.3, random_state = 0)

from sklearn.svm import SVC
classifier = SVC(kernel='linear', random_state=1, C=2)
classifier.fit(f_train, t_train)

predictions = classifier.predict(f_test)

from sklearn.metrics import confusion_matrix, accuracy_score
precision = accuracy_score(t_test, predictions)
matrix = confusion_matrix(t_test, predictions)

import collections
collections.Counter(t_test)