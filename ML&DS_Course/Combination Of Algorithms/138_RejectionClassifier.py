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
response_rf = rf.predict(new_register)
response_mlp = mlp.predict(new_register)

probability_svm = svm.predict_proba(new_register)
confiance_svm = probability_svm.max()

probability_rf = rf.predict_proba(new_register)
confiance_rf = probability_rf.max()

probability_mlp = mlp.predict_proba(new_register)
confiance_mlp = probability_mlp.max()

pay = 0
not_pay = 0
minimal_confiance = 0.9999999

if confiance_svm > minimal_confiance:
    if response_svm[0] == 1:
        pay += 1
    else:
        not_pay += 1

if confiance_rf > minimal_confiance:
    if response_rf[0] == 1:
        pay += 1
    else:
        not_pay += 1
        
if confiance_mlp > minimal_confiance: 
    if response_mlp[0] == 1:
        pay += 1
    else:
        not_pay += 1
    
# Estrategy: Plurality (Most Votes)
if pay >= not_pay:
    print("Client pays")
else:
    print("Client doesn't pay")