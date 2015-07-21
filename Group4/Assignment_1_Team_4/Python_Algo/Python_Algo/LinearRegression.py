# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 19:04:04 2015

@author: insignia
"""

import numpy as np
from sklearn import linear_model
from sklearn import cross_validation
from sklearn import preprocessing

f = open("/Users/insignia/Desktop/Big_Data_Analytics/Assignment/winequality-white_multi.csv")
f.readline()  # skip the header
data = np.loadtxt(f,delimiter=';')


train, test = cross_validation.train_test_split(data, train_size=0.6, test_size=0.4)
X = train[:, 0:10] 
scaler = preprocessing.StandardScaler().fit(X)

X = scaler.transform(X)
y = train[:, 11]
A = test[:, 0:10] 
A = scaler.transform(A)
b = test[:, 11]
clf = linear_model.LinearRegression(normalize=True)
clf.fit(X,y)
train_score= clf.score(X, y)
test_score=clf.score(A,b)
print train_score, test_score

