# -*- coding: utf-8 -*-
import pandas as pd

path = '..\\Data\\credit_risk_data.csv'
df = pd.read_csv(path)
features = df.iloc[:,0:4].values
target = df.iloc[:,4].values
                  
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:,0] = labelencoder.fit_transform(features[:,0])
features[:,1] = labelencoder.fit_transform(features[:,1])
features[:,2] = labelencoder.fit_transform(features[:,2])
features[:,3] = labelencoder.fit_transform(features[:,3])

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(features, target)
print(classifier.intercept_) # bo
print(classifier.coef_) # b1, b2, ..., bn

result = classifier.predict([[0,0,1,2],[3,0,0,0]])
result_2 = classifier.predict_proba([[0,0,1,2],[3,0,0,0]]) # Probability
print(result)
print(result_2)

# result_2:
#
#  x   y
#  z   w
#
# x -> Probabilidade de [0,0,1,2] ser baixo  
# y -> Probabilidade de [0,0,1,2] ser alto
# z -> Probabilidade de [3,0,0,0] ser baixo  
# w -> Probabilidade de [3,0,0,0] ser baixo  