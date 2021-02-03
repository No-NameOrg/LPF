import os
import re
import pickle

import numpy as np
import pandas as pd

from sklearn.linear_model import LogisticRegression

import dataMunging

class LogRegWrapper:

    def __init__(self):
        self.__model = None
        self.__subfolder = 'logreg'
        self.__filePrefix = 'logreg'
        
        if not os.path.exists(self.__subfolder):
            os.mkdir(f'.\\{self.__subfolder}')
    
    def train(self):
        COLS_TO_REMOVE = []
        with open(r'.\cols_to_remove.txt') as file:
            COLS_TO_REMOVE = file.read().replace(" ","").split(",")
        
        data = pd.read_csv(r'.\data\loan-dataset.csv')
        X,y = data.drop(COLS_TO_REMOVE + ['loanid','loanstatus'], axis=1), data.loc[:,'loanstatus'].map({'Y':0,'N':1}).astype('uint8')

        X = self.__preProcess(X, exec_type='train')

        self.__model = LogisticRegression()
        self.__model.fit(X,y)

        pickle.dump(self.__model, open(f'..\\pickle-models\\{self.__filePrefix}-model.pkl', 'wb'))

    def predict(self, X):
        """
            :param:
                X - a dictionary with key as column name and value as column value
        """
        
        data = self.__preProcess(X, 'test')
        
        if not self.__model :
            self.__model = pickle.load(open(f'..\\pickle-models\\{self.__filePrefix}-model.pkl','rb'))

        noProb = self.__model.predict_proba(data)[0,1]

        return 'Y' if noProb <= 0.4 else 'N'

    def __preProcess(self, X, exec_type):

        data = pd.DataFrame(X, index=[0]) if exec_type == 'test' else X

        data.columns = list(map(lambda col: re.sub(r"\W|_","",col.lower()),data.columns))

        data = dataMunging.basicMunging(data,imputeCredit_History=False)
        
        data = dataMunging.createDummiesExcept(data=data,filePrefix=f'{self.__subfolder}\\{self.__filePrefix}',exec_type=exec_type)
        dataMunging.minMaxScaler(data, ['loanamount', 'loanamountterm'], filePrefix=f'{self.__subfolder}\\{self.__filePrefix}',exec_type=exec_type)

        return data

if __name__ == '__main__':
    obj = LogRegWrapper()
    obj.train()
    # print(obj.predict({
    #     'married':'Yes',
    #     'dependents':'1',
    #     "applicantincome":1000,
    #     'coapplicantincome':50,
    #     'loanamount':100,
    #     'loanamountterm':36,
    #     'credithistory':1,
    #     'propertyarea':'Urban'
    # }))