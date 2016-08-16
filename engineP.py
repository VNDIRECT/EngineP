# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:38:25 2016

@author: phucn_000, chau.hoang
"""
import finfo
import statistics
from scipy.stats import norm
import numpy as np
import math

price_stash = finfo.PriceStash()

def compute(myP, cash=0):
    amt_cash = cash

    # toggle this to get real time price
    price = price_stash.build_stash(myP.keys())

    #PORTFOLIO VALUE HISTORY
    _portfolio_series = [[p * myP.get(symbol) for p in price.get(symbol)] for symbol in myP.keys()]
    portfolio = [sum(s) + amt_cash for s in zip(*_portfolio_series)]

    #GET WEIGHTT
    value_portfolio = sum([myP[symbol] * price.get(symbol)[0] for symbol in myP.keys()]) + amt_cash

    weight_P = {}
    for s in myP.keys():
        weight_P[s] = myP[s] * price.get(s)[0]/value_portfolio

    def get_expectedreturn (prices):
        period = int(math.ceil(len(prices)/12))
        average_end = sum(prices [0:period]) /period
        average_begin = sum(prices[len(prices)-period:len(prices)-1]) / period
        return_s = (average_end - average_begin)/average_begin
        return return_s

    return_portfolio = sum([get_expectedreturn(price.get(symbol)) * weight_P.get(symbol) for symbol in myP.keys()])

    #GET PERFORMANCE
    def get_performance (price_history):
        performance = []
        for i in range(0,len(price_history)-2):
            instance = (price_history[i]/price_history[i+1])-1
            performance.append(instance)
        return performance


    #GET VALUE AT RISK

    def get_var(portfolio_performance):
        mean_portfolio = sum(portfolio_performance) / float(len(portfolio_performance))
        std_portfolio = statistics.stdev(portfolio_performance)
        confidence_level = 0.95
        min_return =  norm.ppf(1-confidence_level,mean_portfolio,std_portfolio)
        position_var = value_portfolio *(min_return+1)
        var_portfolio = value_portfolio - position_var
        return var_portfolio

    var_portfolio = get_var(get_performance(portfolio))

    #GET BETA
    def get_beta(x):
        return np.cov(get_performance(price.get('VNINDEX')),get_performance(x))[1][0]/np.var(get_performance(price.get('VNINDEX')))

    beta_portfolio = sum([get_beta(price.get(symbol)) * weight_P.get(symbol) for symbol in myP.keys()])

    #GET MAXIMUM DRAW DOWN
    def get_maxdd (x):
        highest = [0]
        for i in range (0,len(x)):
            max_num = max(x[len(x)-1-i],highest[0])
            highest.insert(0,max_num)
        dd = [0]

        for i in range (0,len(x)):
            if x[len(x)-1-i] == highest[i]:
                dd.insert(0,0)
            else: dd.insert(0,max(dd[i],highest[i]-x[len(x)-1-i]))

        return max(dd)

    maxdd_portfolio = get_maxdd(portfolio)

    return {
        'expectedReturn': return_portfolio,
        'beta': beta_portfolio,
        'valueAtRisk': var_portfolio,
        'maxDrawDown': maxdd_portfolio
    }

