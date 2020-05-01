# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv('Data\\credit_data.csv')

features = df.iloc[:, 1:4].values
target = df.iloc[:,4].values

from sklearn.preprocessing import Imputer

imputer = Imputer(missing_values = 'NaN', strategy='mean', axis=0)
imputer = imputer.fit(features[:, 1:4])
features[:, 1:4] = imputer.transform(features[:, 1:4])

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
previsores = scaler.fit_transform(features)

from sklearn.model_selection import train_test_split
f_train, f_test, t_train, t_test = train_test_split(features, target, test_size = 0.25, random_state=0)

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion='entropy', random_state=0) # Random state = 0 -> stabilizes at a value
classifier.fit(f_train, t_train)
predictions = classifier.predict(f_test)

from sklearn.metrics import confusion_matrix, accuracy_score
precision = accuracy_score(t_test, predictions)
matrix = confusion_matrix(t_test, predictions)

