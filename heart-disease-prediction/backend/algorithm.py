# -*- coding: utf-8 -*-
"""Proj.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12TDvpqINEhSWkEg73eHsg5gi_FlvdzuJ
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv('heart_disease_data.csv')

df.head()

df.tail()

df.shape

df.info()

df.describe()

df['target'].value_counts()

"""#1: Defective Heart
#0: Healthy Heart
"""

X = df.drop(columns='target',axis=1)

X

Y = df['target']

Y

"""**SPLITTING DATASET INTO TRAIN AND TEST**"""

X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.2,stratify=Y,random_state=23)

print(X_test.shape, X_train.shape)

"""#MODEL TRAINNING"""

model = LogisticRegression()

#Train the model with Training data
model.fit(X_train,Y_train)

Y_pred = model.predict(X_test)

Y_train

score = accuracy_score(Y_test,Y_pred)

print("The accuracy score is", score)

"""BUILDING A PREDICTIVE **SYSTEM**"""

input_data = (62, 0, 0, 140, 268, 0, 0, 160, 0, 3.6, 0, 2, 2)
#Change the input_data into array
arr = np.array(input_data)

print(arr)

prediction = model.predict(arr.reshape(1,-1))

print(prediction)

if prediction == 0:
  print("The person does not have a heart disease")
else:
  print("The person has a heart disease")

