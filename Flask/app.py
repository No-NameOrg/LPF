from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import json
import os
import sys
from LogRegWrapper import LogRegWrapper

# insert at 1, 0 is the script path (or '' in REPL)
# sys.path.insert(1,'/LPF')

app = Flask(__name__)
# os.system('python DefaultCreditCard.py')

# modelfile = 'models/log-reg-wrapper.pkl'
# model = p.load(open(modelfile, 'rb'))
    
@app.route('/', methods=['POST'])
def makecalc():
    data = request.get_json()
    print(data)
    prediction = LogRegWrapper().predict(data)
    # response = jsonify(prediction)
    
    # response.headers.add('Access-Control-Allow-Origin', 'http://127.0.0.1:5000/')
    # response.headers.add('Access-Control-Allow-Credentials', 'true')
    # return prediction
    return jsonify(result=prediction)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)