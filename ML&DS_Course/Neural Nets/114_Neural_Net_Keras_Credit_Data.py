# -*- coding: utf-8 -*-

import pandas as pd
from keras.models import Sequential
from keras.layers import Dense # Dense Neural Net -> All connections between neurons

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

from sklearn.model_selection import train_test_split
f_train, f_test, t_train, t_test = train_test_split(features, target, test_size = 0.3, random_state=0)

classifier = Sequential()

# Creating Layers

# Units = number neurons
classifier.add(Dense(units=2, activation = 'relu', input_dim = 3))
classifier.add(Dense(units=2, activation = 'relu'))
classifier.add(Dense(units=1, activation = 'sigmoid')) # Output Layer
classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

classifier.fit(f_train, t_train, batch_size=10, nb_epoch=100) # nb_epoch = Execute 100 times the error atualization
predictions = classifier.predict(f_test)
predictions = (predictions > 0.5)

from sklearn.metrics import confusion_matrix, accuracy_score
precision = accuracy_score(t_test, predictions)
matrix = confusion_matrix(t_test, predictions)