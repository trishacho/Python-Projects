from sklearn.datasets import load_iris
from sklearn import tree
from sklearn.model_selection import train_test_split
import collections
import graphviz #to visualize decision trees
import pandas as pd

import os
os.environ["PATH"] += os.pathsep + '/opt/homebrew/bin/'

df = pd.read_csv('training set copy 3.csv')

import csv
filename = 'training set copy 3.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    X = []
    Y = []
    for row in reader:
        classifications = row[6]
        values = row[1:6]
        X.append(values)
        Y.append(classifications)

X = [[float(x) for x in X] for X in X]

data_feature_names = df.columns.tolist()
items_to_remove = ['Pizza', 'Classification']
data_feature_names = [item for item in data_feature_names if item not in items_to_remove]
print(data_feature_names)


# Training
clf = tree.DecisionTreeClassifier()
#clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X,Y)


# Visualize data
dot_data = tree.export_graphviz(clf,
                               feature_names=data_feature_names,
                               out_file=None,
                               filled=True,
                               rounded=True,
                               class_names=['Chicago', 'New York', 'Rhode Island', 'St. Louis'])

graph = graphviz.Source(dot_data)
graph.render('dtree',view=True)
