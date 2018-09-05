#!/usr/bin/python
# *-- encoding:utf-8 --*
""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
import sys
sys.path.append("../final_project/")
sys.path.append("../tools/")
import pickle
from feature_format import featureFormat,targetFeatureSplit

f = open("../final_project/poi_names.txt","r+")
'''
for i in f.readlines():
    print i
'''
f.close()

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# s = 'Jeffrey Skilling'
# print ' '.join(s.upper().split(' ')[::-1])


def cal(str1):
    i = 0
    j = 0
    s1 = ' '.join(str1.upper().split(' ')[::-1])
    for key in enron_data:
        if s1 in key:
            print key
            print enron_data[key]['total_payments']
            print '-----'
        if enron_data[key]['email_address'] != 'NaN':
            i += 1
        if enron_data[key]['salary'] != 'NaN':
            j += 1
        # for key1 in enron_data[key]:
        #    print key1
    print i
    print j
# cal('ss')

print enron_data['COLWELL WESLEY']['from_this_person_to_poi']

def selectfeatures():
    features_list = []
    # add features
    for key in enron_data:
        for features1 in enron_data[key]:
            features_list.append(features1)
        break
    index = features_list.index('poi')
    features_list.insert(0,features_list[index])
    del features_list[index+1]
    del features_list[features_list.index('email_address')]
    # print features_list
    data_array = featureFormat(enron_data,features_list,remove_NaN=True)
    label, features = targetFeatureSplit(data_array)

    return label,features
label, features = selectfeatures()
# print label,'\n',features
print '已知的poi人数:',sum(label)