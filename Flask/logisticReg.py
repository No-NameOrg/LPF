
import pickle

import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

import dataMunging
import utils

# NOTE: It is assumed that the file is run from the root
COLS_TO_REMOVE = []
with open(r'.\src-code\cols_to_remove.txt') as file:
    COLS_TO_REMOVE = file.read().replace(" ","").split(",")

dataset = pd.read_csv(r"loan-dataset.csv")
dataset = dataMunging.basicMunging(dataset,"processed-dataset.csv",imputeCredit_History=False)
X, y = dataset.drop(COLS_TO_REMOVE + ['loanid', 'loanstatus'], axis=1), dataset.loc[:, 'loanstatus'].map({'Y':0,'N':1}).astype('uint8')

X = dataMunging.createDummiesExcept(data=X, exec_type='train')
dataMunging.minMaxScaler(X, ['loanamount', 'loanamountterm'], exec_type='train')

logReg = LogisticRegression()
logReg.fit(X, y)

pickle.dump(logReg, open(r'.\pickle-models\logReg-model.pkl', 'wb'))
