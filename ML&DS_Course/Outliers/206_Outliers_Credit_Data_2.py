# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv("..//Data//credit_data.csv")
df = df.dropna()
df.loc[df.age < 0, "age"] = 40.92 # 40.92 = Average

import matplotlib.pyplot as plt

# Income x Age
plt.scatter(df.iloc[:,1], df.iloc[:,2])

# Income x Loan
plt.scatter(df.iloc[:,1], df.iloc[:,3])

# Age x Loan
plt.scatter(df.iloc[:,2], df.iloc[:,3])

census = df = pd.read_csv("..//Data//census_data.csv")

plt.scatter(census.iloc[:,0], census.iloc[:,2])