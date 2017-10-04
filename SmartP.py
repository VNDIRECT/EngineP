# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:38:25 2016

@author: phucn_000
"""
import json
from engineP import compute
from portopt import markowitz
import finfo
from error import CommonError

from flask import Flask, request, jsonify
from crossdomain import crossdomain
import time

app = Flask(__name__)

def parse_portfolio(request):
    symbols = request.args.get('symbols').split(',')
    quantities = map(int, request.args.get('quantities').split(','))
    cash_param = request.args.get('cash')
    cash = int(cash_param) if cash_param is not None else 0
    if len(symbols) != len(quantities):
        raise 'symbols and quantities must be of the same length'
    myP = {k: v for k,v in zip(symbols, quantities)}
    return myP, cash

@app.route("/")
@crossdomain(origin="*")
def hello():
    # try:
    portfolio, cash = parse_portfolio(request)
    return json.dumps(compute(portfolio, cash))
    # except Exception as e:
    #     raise CommonError(e.message)

@app.route("/markowitz")
@crossdomain(origin="*")
def markowitz_endpoint():
    # try:
    portfolio, cash = parse_portfolio(request)
    return json.dumps(markowitz(portfolio, cash))
    # except Exception as e:
    #     raise CommonError(e.message)

## Currently not working, should fork another process instead
# @app.route("/refresh")
# @crossdomain(origin="*")
# def refresh_price():
#     """
#     This endpoint refresh all price data
#     """
#     try:
#         price = finfo.PriceStash()
#         price.full_refetch()
#         return jsonify({'status': 'OK'})
#     except Exception as e:
#         raise CommonError('Error while refresh: {}'.format(e.message))

# @app.errorhandler(CommonError)
# def handle_error(error):
#     response = jsonify(error.to_dict())
#     response.status_code = error.status_code
#     return response

@app.route("/error")
@crossdomain(origin="*")
def error_endpoint():
    raise CommonError('This endpoint has an error')

if __name__ == "__main__":
    app.run(host='0.0.0.0', threaded=True, debug=True)


