#Import all necessary python libraries

import numpy as np
from numpy import mean
from numpy import std
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.datasets import make_classification
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import StratifiedKFold
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import cross_validate
from sklearn.calibration import CalibratedClassifierCV
from sklearn.calibration import calibration_curve

#Load the data

df = pd.read_excel(r'//Users//sayanbiswas//Desktop//CSDH ML Project//Final ML CSDH dataset.xlsx') #--> change the directory to your own inorder to read the document
df = df.sample(frac = 1)

Z = df.drop(['Registrar Taking Referral', 'Consultant'], axis = 1)
X = df.drop(['Registrar Taking Referral', 'Consultant', 'Acceptance Status'], axis = 1)
Y = df['Acceptance Status']
object = StandardScaler()
X[['GCS']] = object.fit_transform(df[['GCS']])
X[['Age']] = object.fit_transform(df[['Age']])

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.20, random_state=42)

KFolds = RepeatedStratifiedKFold(n_splits=4, n_repeats=4, random_state=420)

#Create the model, train it and test it

model = LogisticRegression(max_iter=1000)

calibrated = CalibratedClassifierCV(model, method='sigmoid', cv=KFolds, ensemble=True)
calibrated = calibrated.fit(X_train, Y_train)
# predict probabilities
probs = calibrated.predict_proba(X_test)[:, 1]
# reliability diagram
#fop, mpv = calibration_curve(Y_test, probs, n_bins=10, normalize=True)
#print(probs)

#Export the model with pickle

import pickle
filename = 'finalized_model.sav'
pickle.dump(calibrated, open(filename, 'wb'))

#Load in the saved model

loaded_model = pickle.load(open(filename, 'rb'))
result = loaded_model.score(X_test, Y_test)
print(result) #--> outputs the accuracy of the model on the test set

#Give the model an input to determine the output

input = [[60, 1, 0, 0, 15, 0, 1, 3, 0, 0]]
result = loaded_model.predict_proba(input)

'''
if result > 0.5:
    print("Accepted")
else:
    print("Rejected")
'''
print(result) #--> outputs the result of the given input

#The output should be a probability and if it more than 0.5, then the patient is accepted
#The ANN model outputs a probability more than 0.5 and the patient is accepted