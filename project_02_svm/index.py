#!/usr/bin/python
# -*- coding: utf-8 -*-
""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
  
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# Reduzindo o tamanho do data set para fazer teste
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

# clf = SVC(kernel="linear")
clf = SVC(kernel="rbf", C=10000.)
t0 = time()
clf.fit(features_train, labels_train)
print "tempo de treinamento:", round(time()-t0, 3), "s"


t1 = time()
pred = clf.predict(features_test)
print "tempo de predição:", round(time()-t1, 3), "s"


count_zero = 0
count_one = 0
for val in pred:
    if val == 0:
        count_zero += 1
    else:
        count_one += 1


print accuracy_score(pred, labels_test)
print "Count values"
print count_zero
print count_one