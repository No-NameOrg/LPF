from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
import os
import sys

from LogRegWrapper import LogRegWrapper
from DecisionTreeWrapper import DecisionTreeWrapper


app = Flask(__name__)

@app.route('/', methods=['POST'])
def makecalc():
    data = request.get_json()
    logPred = LogRegWrapper().predict(data)
    decPred = DecisionTreeWrapper().predict(data)
    
    return jsonify(
        logPred = logPred,
        DecPred = decPred
    )

if __name__ == '__main__':
    # os.system('python LogRegWrapper.py')
    # os.system('python DecisionTreeWrapper.py')
    app.run(threaded=True, port=5000)