# -*- coding: utf-8 -*-
# With orange, we don't have to deal with missing values

import Orange

# i#columnname -> Ignores thye column

data = Orange.data.Table("Data\\credit_data.csv")
print(data.domain)

divided_data = Orange.evaluation.testing.sample(data, n=0.25)
data_training = divided_data[1]
data_test = divided_data[0]
print(len(data_training), len(data_test))

cn2_learner = Orange.classification.rules.CN2Learner()
classifier = cn2_learner(data_training)

for rule in classifier.rule_list:
    print(rule)
    
# We can predict with more than one classifier
result = Orange.evaluation.testing.TestOnTestData(data_training, data_test, [lambda testdata: classifier])
print(Orange.evaluation.CA(result)) # Review this. It could be a bug in the library