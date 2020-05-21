# -*- coding: utf-8 -*-
import pandas as pd
import apyori as ap
 
data = pd.read_csv("Data\\market_1.csv", header = None)

transactions = []

for i in range(10):
    transactions.append([str(data.values[i,j]) for j in range (4)])
    
from apyori import apriori
rules = apriori(transactions, min_support = 0.3, min_confidence = 0.8, min_lift = 2, min_length = 2)

results_1 = list(rules)
print(results_1)

results_2 = [list(x) for x in results_1]
print(results_2)

formatedResults = []
for j in range(3):
    formatedResults.append([list(x) for x in results_2[j][2]])

print(formatedResults)