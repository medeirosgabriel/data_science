# -*- coding: utf-8 -*-
import pandas as pd
import apyori as ap
 
data = pd.read_csv("Data\\market_2.csv", header = None)

transactions = []

for i in range(7501):
    transactions.append([str(data.values[i,j]) for j in range (20)])

# support -> (vendaspDia * Dias)/TotalRegistros
# 0.003 = (4 * 7)/7501
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

results_1 = list(rules)
print(results_1)

results_2 = [list(x) for x in results_1]
print(results_2)

formatedResults = []
for j in range(5):
    formatedResults.append([list(x) for x in results_2[j][2]])

print(formatedResults)