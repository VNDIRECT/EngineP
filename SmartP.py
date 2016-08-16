# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:38:25 2016

@author: phucn_000
"""
import json
from engineP import compute
from portopt import markowitz
from flask import Flask, request
from crossdomain import crossdomain
import time

app = Flask(__name__)

@app.route("/")
@crossdomain(origin="*")
def hello():
    try:
        symbols = request.args.get('symbols').split(',')
        quantities = map(int, request.args.get('quantities').split(','))
        cash_param = request.args.get('cash')
        cash = int(cash_param) if cash_param is not None else 0
        if len(symbols) != len(quantities):
            raise 'symbols and quantities must be of the same length'
        myP = {k: v for k,v in zip(symbols, quantities)}
        return json.dumps(compute(myP, cash))
    except Exception as e:
        print('error', e)
        return json.dumps({
                'error': e.message
            }), 500

@app.route("/markowitz")
@crossdomain(origin="*")
def markowitz_endpoint():
    try:
        symbols = request.args.get('symbols').split(',')
        return json.dumps(markowitz(symbols))
    except Exception as e:
        print('error', e)
        return json.dumps({
                'error': e.message
            }), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0')


