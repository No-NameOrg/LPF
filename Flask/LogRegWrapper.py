import re
import pickle

import numpy as np
import pandas as pd

import dataMunging
import utils

class LogRegWrapper:

    def __init__(self):
        self.__model = pickle.load(open(r'.\pickle-models\logReg-model.pkl','rb'))

    def predict(self, X):
        """
            :param:
                X - a dictionary with key as column name and value as column value
        """
        
        data = self.__preProcess(X)
        noProb = self.__model.predict_proba(data)[0,1]

        return 'Y' if noProb <= 0.5 else 'N'

    def __preProcess(self, X):

        data = pd.DataFrame(X, index=[0])
        data.columns = list(map(lambda col: re.sub(r"\W|_","",col.lower()),data.columns))

        data = dataMunging.basicMunging(data,imputeCredit_History=False)
        
        data = dataMunging.createDummiesExcept(data=data,exec_type='test')
        dataMunging.minMaxScaler(data, ['loanamount', 'loanamountterm'], exec_type='test')

        return data


if __name__ == '__main__':
    obj = LogRegWrapper()
    pickle.dump(obj, open('log-reg-wrapper.pkl','wb'))