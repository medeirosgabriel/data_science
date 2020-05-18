# -*- coding: utf-8 -*-

import pickle
from sklearn.preprocessing import StandardScaler
import numpy as np

svm = pickle.load(open("..\\Algorithm Evaluation\\Models\\svm.sav", 'rb'))
rf = pickle.load(open("..\\Algorithm Evaluation\\Models\\random_forest.sav", 'rb'))
mlp = pickle.load(open("..\\Algorithm Evaluation\\Models\\mlp.sav", 'rb'))

new_register=[[50000, 40, 5000]]
new_register = np.asarray(new_register)
new_register = new_register.reshape(-1,1)

scaler = StandardScaler()
new_register = scaler.fit_transform(new_register)
new_register = new_register.reshape(-1,3)

response_svm = svm.predict(new_register)
response_random = rf.predict(new_register)
response_mlp = mlp.predict(new_register)

pay = 0
not_pay = 0

if response_svm == 1:
    pay += 1
else:
    not_pay += 1
    
if response_random == 1:
    pay += 1
else:
    not_pay += 1
    
if response_mlp == 1:
    pay += 1
else:
    not_pay += 1
    
# Estrategy: Plurality (Most Votes)
if pay >= not_pay:
    print("Client pays")
else:
    print("Client doesn't pay")