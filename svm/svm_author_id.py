#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
import numpy as np
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
features_train = features_train[:len(features_train)/100]
labels_train = labels_train[:len(labels_train)/100]
def SVM_classification(features_train, features_test, labels_train, labels_test):
    model = SVC(kernel='rbf',C=10000)
    # t0 = time()
    model.fit(features_train, labels_train)
    # print "training time:", round(time() - t0, 3), "s"
    # t1 = time()
    predict = model.predict(features_test)
    print type(predict)
    print predict.shape
    print predict.dtype
    # print "testing time:", round(time() - t1, 3), "s"
    # l = [10,26,50]
    # print predict[l]

    print sum(predict)

    acc = accuracy_score(labels_test, predict,normalize=False)
    return acc


acc = SVM_classification(features_train, features_test, labels_train, labels_test)
print acc


#########################################################
### your code goes here ###

#########################################################


