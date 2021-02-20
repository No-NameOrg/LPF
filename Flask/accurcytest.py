import pickle
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from LogRegWrapper import LogRegWrapper
from DecisionTreeWrapper import DecisionTreeWrapper
import utils as utils

import warnings
warnings.simplefilter("ignore")

data = pd.read_csv(r'data\loan-dataset.csv')

COLS_TO_REMOVE = []

with open(r'.\cols_to_remove.txt') as file:
    COLS_TO_REMOVE = file.read().replace(" ","").split(",")

X,y = data.drop(COLS_TO_REMOVE + ['loanid','loanstatus'], axis=1), data.loc[:,'loanstatus'].map({'Y':0,'N':1}).astype('uint8')

trainX, testX, trainY, testY = train_test_split(X, y, test_size=0.2,random_state=0)

logWrapper = LogRegWrapper()
logWrapper.train(trainX, trainY)

print(logWrapper.score(testX, testY))
# predY = logWrapper.predictProba(testX)
# utils.precisionRecall(testY, predY)
# utils.drawROC(testY, predY)