# -*- coding: utf-8 -*-

import Orange

# i#columnname -> Ignores the column
# c#columnname -> Target variable
# Put in the data to avoid error

data = Orange.data.Table('..\\Data\\credit_risk_data.csv')
print(data.domain)

cn2_learner = Orange.classification.rules.CN2Learner() # Algothm

# classifier = cn2_learner(data) Error, because orange doesn't know who the class is
# To fix the error, it is necessary change the target column to 'c#columnname'

classifier = cn2_learner(data)

for rule in classifier.rule_list:
    print(rule)

# The last rule is the default rule
    
result = classifier([['boa', 'alta', 'nenhuma', 'acima_35'], ['ruim', 'alta', 'adequada', '0_15']])

for r in result:
    print(r)
    
for r in result:
    print(data.domain.class_var.values[r])
    
print(data.domain)

