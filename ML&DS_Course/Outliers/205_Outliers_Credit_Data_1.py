# -*- coding: utf-8 -*-

import pandas as pd

df = pd.read_csv("..//Data//credit_data.csv")

df = df.dropna()

# Age outliers
import matplotlib.pyplot as plt
plt.boxplot(df.iloc[:,2], showfliers = True)
outliers_age = df[(df.age < -20)]

# Loan outliers
import matplotlib.pyplot as plt
plt.boxplot(df.iloc[:,3])
outliers_age = df[(df.loan > 13400)]