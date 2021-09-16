import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.svm import LinearSVC


csv = pd.read_csv('dataset.csv')

# check repeating data:
if csv.duplicated().sum():
    print(f'There is {csv.duplicated().sum} no.of duplicate')
    csv = csv.drop_duplicates()
else:
    print('No duplicated')

# drop Null row
if any(csv.isna().any(axis=1)):
    print(f'There is {csv.isna().any(axis=1).sum()} no. of null')
    csv = csv.dropna()
else:
    print('No null value')

# SVM
x = csv.target.to_numpy()
y = csv.drop(columns='target').to_numpy()

# split train and test into 0.8 0.2
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


# Training algorithm
svclassifier = LinearSVC(dual=False)
svclassifier.fit(x_train, y_train)


# Prediction Classes
y_pred = svclassifier.predict(x_test)

# Evalute the model
print(classification_report[y_test, y_pred])

print()