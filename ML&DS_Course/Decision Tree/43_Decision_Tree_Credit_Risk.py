# -*- coding: utf-8 -*-
import pandas as pd

path = 'Data\\credit_risk_data.csv'
df = pd.read_csv(path)
features = df.iloc[:,0:4].values
target = df.iloc[:,4].values
                  
from sklearn.preprocessing import LabelEncoder
labelencoder = LabelEncoder()
features[:,0] = labelencoder.fit_transform(features[:,0])
features[:,1] = labelencoder.fit_transform(features[:,1])
features[:,2] = labelencoder.fit_transform(features[:,2])
features[:,3] = labelencoder.fit_transform(features[:,3])

from sklearn.tree import DecisionTreeClassifier

classifier = DecisionTreeClassifier(criterion='entropy')
classifier.fit(features, target)
print(classifier.feature_importances_)

# Graph -> Need GraphViz
# export.export_graphviz(classifier, out_file = 'arvore.dot', 
#                        features_names = ['historia', 'divida', 'garantias', 'renda'], 
#                        class_names = ['alto', 'moderado', 'baixo'], 
#                        filled = True, 
#                        leaves_parallel = True)

result = classifier.predict([[0,0,1,2], [3,0,0,0]])
print(classifier.classes_)
