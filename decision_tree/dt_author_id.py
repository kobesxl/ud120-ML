#!/usr/bin/python
# -- encoding:utf-8 --
""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

# print numbers of features used
# print len(features_train[0])


#########################################################
### your code goes here ###

###   DecisionTreeClassifier(criterion = "gini", splitter="best", max_depth=None, min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0,
###   max_features=None, random_state=None, max_leaf_nodes=None, min_impurity_decrease=0.0, min_impurity_split=None, class_weight=None, presort=False)
###   min_samples_split = 2 最小的数需要继续分类的样本数（如果为2，那就表示，低于2的样本可以不用继续拆分，高于2的需要继续拆分）
###   min_samples_leaf = 1 最小的叶子数量
###
def decisionclf(features_train, features_test, labels_train, labels_test):
    clf = DecisionTreeClassifier(min_samples_split=40)
    clf.fit(features_train,labels_train)
    pred = clf.predict(features_test)
    acc = accuracy_score(y_true=labels_test, y_pred=pred)
    return acc
#########################################################


print decisionclf(features_train, features_test, labels_train, labels_test)


