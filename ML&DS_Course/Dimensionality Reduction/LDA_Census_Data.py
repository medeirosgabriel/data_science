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

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
features = scaler.fit_transform(features)

from sklearn.model_selection import train_test_split
f_train, f_test, t_train, t_test = train_test_split(features, target, test_size = 0.15, random_state = 0)

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
lda = LinearDiscriminantAnalysis(n_components = 2); # 6 principal components
f_train = lda.fit_transform(f_train)
f_test = lda.transform(f_test)

from sklearn.ensemble import RandomForestClassifier
classifier = RandomForestClassifier(n_estimators=40, criterion='entropy', random_state=0)
classifier.fit(f_train, t_train)
predictions = classifier.predict(f_test)

from sklearn.metrics import confusion_matrix, accuracy_score
precision = accuracy_score(t_test, predictions)
matrix = confusion_matrix(t_test, predictions)

# Base Line = Help to evaluate the models
# Calculus = most_commom/rest
from collections import Counter
print(Counter(t_test))