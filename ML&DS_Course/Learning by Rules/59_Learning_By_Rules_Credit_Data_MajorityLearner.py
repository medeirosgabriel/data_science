# -*- coding: utf-8 -*-

import Orange
 
data = Orange.data.Table('Data\\credit_data.csv')
print(data.domain)
 
divided_data = Orange.evaluation.testing.sample(data, n=.25)
data_training = divided_data[1]
data_test = divided_data[0]
len(data_training)
len(data_test)

# Since most are equal to class 0, everyone is classified with this class
#Way 1
classifier = Orange.classification.MajorityLearner()
resultado = Orange.evaluation.testing.TestOnTestData(data_training, data_test, [classifier])
print(Orange.evaluation.CA(resultado))
 
 
#Way 2
classifier = classifier(data_training)
result_2 = classifier(data_test)
 
from sklearn.metrics import accuracy_score
precision = accuracy_score(data_test[:,3], result_2)
print(precision)

# Base Line = Help to evaluate the models
from collections import Counter
quant = Counter(str(d.get_class()) for d in data_test)
print(quant, quant['0']/(quant['0'] + quant['1'])) # Accuracy Calculus


