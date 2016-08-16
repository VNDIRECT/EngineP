# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:38:25 2016

@author: phucn_000
"""
import json
from engineP import compute
from flask import Flask, request
from crossdomain import crossdomain




app = Flask(__name__)

@app.route("/")
@crossdomain(origin="*")
def hello():
    symbols = request.args.get('symbols').split(',')
    quantities = map(int, request.args.get('quantities').split(','))
    if len(symbols) != len(quantities):
        return json.dumps({
                error: 'symbols and quantities must be of the same length'
            })
    myP = {k: v for k,v in zip(symbols, quantities)}
    return json.dumps(compute(myP))

if __name__ == "__main__":
    app.run()







