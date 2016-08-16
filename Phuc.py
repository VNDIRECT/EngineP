# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 18:38:25 2016

@author: phucn_000
"""
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()


import statistics
from scipy.stats import norm
import numpy as np
import math
#PRICE HISTORY INPUT
vnindex = [655.7,660.2,648.3,637.3,629.5,627.4,631.9,631.6,636,648.4,652.2,657.1,656.1,648.6,649.3,649.9,659.6,660.3,667.8,673.5,664.6,666.7,675.1,658.9,652.3,658.7,661.1,649.5,650.9,648,640.3,632.3,630.1,622.2,621.3,620.8,632.3,626.4,628,626.5,619.2,625.1,627,625.4,623.6,629.8,631.3,627.9,624.6,620,621.9,623.4,619.9,618.4,614.5,608.1,604.3,611.9,611.6,611,614.8,619.2,622.5,624.8,615.8,610.8,612.1,614.1,605,603.9,606.5,601.5,599.1,598.4,591.7,594,598.5,591.6,592.5,575.7,568,568.3,579.9,579.5,578,579.8,579.3,572.3,571.6,567.8,560.3,555.8,558.4,561.2,569.9,568.3,575.7,572.1,570.7,574.7,570.9,572.3,575.8,579.3,577.1,574,578,577.3,575.9,571.7,574.7,576.2,573.6,570.4,570.2,561.6,559.4,566.1,562.8,568,561.3,560.7,554,552.5,547,548,543.8,544.8,542.1,539.1,536.5,540.6,545.2,539.5,542.7,537.7,542.4,522.2,521.9,529.4,535.8,526.4,543,553,560.4,564.3,557.9,560,565.4,574.6,569.9,574.4,579,579.5,576.3,569.9,567.7,566.2,564.3,566.4,566.9,568.2,577.1,572.5,568,562.2,563.4,561,565.2,574.1,563.6,571.6,574.4,574.4,570.4,573.2,582.9,590.4,595.7,593.8,600,604.5,601.9,603.3,605,609.2,611.3,605.6,603.5,605.3,610.7,612.4,615.2,610.6,611.7,602.8,607.4,605.2,596.2,598.4,598.6,601.7,595.1,590.2,590.5,594.6,593,592.4,590,590.8,592.1,588,586.8,579.6,581.3,570,562.3,563.5,562.6,561.2,564.9,570.4,570.2,572.7,573.2,572.1,566.2,562.5,564.1,563.3,562.2,566.7,572.1,572.3,566.7,554.9,556.8,554.3,562.3,564.8,570.9,555.8,545.9,530,526.9,556.3,566.7,577.8,580.2,573.1]
vnm = [168,169,164,162,158,158,156,154,152,155,158,160,158,157,154,156,157,158,153,150,147,146,147,147,146,147,147,143,144,145,143,141,139,140,137,137,140,139,139,137,137,137,137,137,137,137,138,138,137,136,139,141,141,142,142,143,141,144,145,146,146,145,145,147,146,144,145,146,143,144,142,142,142,139,138,138,140,139,140,137,136,139,143,142,142,143,143,143,141,137,137,134,134,134,136,134,135,134,135,134,133,135,138,138,137,136,135,136,131,131,131,131,132,131,132,130,128,130,129,131,130,130,129,129,130,128,126,124,122,121,119,119,116,116,117,115,118,114,116,117,119,117,120,121,121,123,121,122,124,126,125,126,128,127,127,127,124,125,124,125,125,128,128,128,126,124,123,123,123,125,120,123,123,123,122,124,124,123,125,123,127,131,130,132,134,140,137,132,130,128,127,129,128,123,123,117,118,119,114,114,113,115,114,113,112,111,106,105,106,102,101,101,101,102,103,103,100,101,100,100,102,101,100,101,102,99,98.5,97.5,97.5,97.5,97.5,98.5,99.5,97.5,97,97,98.5,99,99.5,100,101,99.5,100,96,94.5,101,102,104,103,103]
hpg = [45.8,46,45.3,43.3,42.8,43.1,42.6,43.2,42.7,44.1,44.5,44.6,43.2,42.3,40.9,40.2,41.2,41.1,42,42.3,40.6,40.2,41.6,41.1,40.5,42.7,42.8,41,40.2,39.9,39.8,39.6,39.3,38.7,39,38.8,40.1,39.6,39.2,38.4,37.4,38.1,38,37.9,36.5,37,36.7,36.9,36.3,35.4,35.6,35.2,34.4,33.8,33.8,33.3,33.2,33.7,33.7,33.7,33.2,33.2,33.1,33.6,33.2,33.3,34,34.5,33.5,33.9,34,35,35,33.5,32.5,32.7,33,33,32.7,31.5,31.2,30.9,31.3,31.4,31.1,31.7,31.5,30.8,30.1,30.2,29.3,29.2,29,29.5,29.5,29.8,29.9,29,28.8,29.3,29.5,29.8,29.7,30,29.9,30,30,28.8,28.6,28.5,28.9,27.8,27.5,27,27.2,27.4,27.9,28.4,27.3,27.2,27.2,27.2,27,26.8,26.7,26.7,26.4,27,27,26.8,26.8,26.7,27.5,26.5,26.8,26.4,27.2,25.6,25.5,25.2,25.2,24.8,25.5,26.5,27.5,28,27.7,27.7,28.2,29,28.5,28.8,29.2,29.3,28.9,28.9,29.5,29.5,29.5,29.7,30,30.4,30.4,30.5,30.6,30.6,29.8,29.4,29.8,30.3,29.9,30.3,30.6,30.6,30.3,30.5,31.3,31.7,31.1,30.1,30.2,29.9,29.8,30.1,30.2,29.6,30.1,30.1,30.3,30.5,30.7,31,31,31.1,31.5,31.2,31.5,31.5,31.4,31.7,31.9,31.8,31.4,31.2,31.4,32,32,32.3,32.3,32.4,32.8,32.4,32.2,31.5,32,31.4,30.9,30.7,30.4,30.1,30.2,31.1,31.4,31.6,31.8,31.7,30.8,30,29.7,29.2,29.3,29.7,30.4,30.7,30.2,29.2,29.7,30.1,31.1,31.1,31.6,31.3,31.5,30,28.1,30.2,31.1,31.8,32.1,31.7]
vnd = [12.5,12.8,12.6,12.9,12.8,12.8,12.7,13,13,13.4,13.4,13.4,13.1,13.1,13.1,13.2,13.5,13.8,13.9,13.7,13.6,13.5,13.7,13.6,12.9,13.5,13.7,13.1,13.2,12.8,11.7,11.7,11.4,11.4,11.3,11.3,12,11.9,12.1,12.2,12.1,12.4,12.6,12.6,12.5,12.6,12.2,11.9,11.7,11.7,11.9,12,12,11.8,11.8,11.5,11.4,11.6,11.6,11.6,11.6,11.6,11.8,11.8,11.7,11.6,11.7,11.8,11.8,11.8,11.8,11.7,11.8,11.8,11.7,11.6,11.6,11.9,11.8,11.6,11.5,11.6,11.8,11.9,11.9,12,11.8,11.7,11.8,11.8,11.7,11.2,11.1,11.1,11.3,11.3,11.5,11.5,11.7,11.8,11.9,11.9,11.9,12.2,12,12.1,12.4,12.4,12.4,12,11.9,11.7,11.8,11.8,11.7,11.7,11.8,11.7,11.5,11.9,11.6,11.9,11.3,11.4,11.1,11.3,11.2,11.4,11.2,11,11,11.2,11.5,11.4,11.3,11,11.3,10.8,10.2,10.1,10.2,9.8,10.6,11.1,11.2,11.1,10.7,10.7,11.1,11.6,11.5,11.6,12.1,12.1,11.9,11.3,11.3,11.3,11,11.3,11.5,11.8,12,12.1,11.9,12,12.2,12.2,12.5,12.8,12.6,12.8,12.6,12.6,12.7,12.9,13.2,13.3,13.5,13.7,13.6,13.3,13.1,13.3,13.2,13.2,13.5,13.5,13.4,13.5,13.8,13.8,14.1,14,13.9,13.6,13.8,13.9,13.6,13.7,13.5,13.4,13.4,12.9,12.8,13.3,13.4,13.3,13.1,13.2,13.2,13.1,13.3,13.2,13.4,12.6,12.3,12.3,12.6,12.6,12.8,13.2,13.5,13.6,13.6,13.7,13.5,13.2,13.6,13.5,13.4,13.8,14,14.1,14.1,13.7,13.8,13.7,14.3,14.4,14.3,13.8,13.7,13,13.1,14.5,14.7,15.1,14.4,14.3]
ssi = [21.8,22,21.7,21.4,21.4,21.5,22,22.2,22.1,22.8,22.9,23.2,22.7,22.4,22.3,22.5,23,23.7,24.1,23.7,23.5,23.6,24.1,23.4,23,22.7,22.5,22.4,22.4,22,20.6,20.8,20.9,20.3,20.2,20.3,20.8,20.8,20.9,20.9,20.5,21.2,21.2,21.5,21.6,22,21.8,21.5,21.2,21.1,21.3,21.4,21.3,21.5,21.6,20.8,20.5,20.6,20.7,20.8,20.7,20.6,20.7,20.8,20.6,20.2,20.4,20.4,20.8,21.2,21.4,21.4,21.4,21.4,21.7,21.9,22.4,22.1,21.5,21.2,21.2,21.3,21.6,21.7,21.7,21.8,21.9,21.7,21.9,21.8,21.7,21.3,21.2,21.1,21.3,21.1,21.6,21.6,21.8,21.7,21.6,22,22,22.2,22.3,22.5,22.7,22.8,22.9,22.5,22.4,22.7,22.8,23.1,23.2,22.7,22.5,22.5,22.4,22.8,22.4,22.3,21.2,21.2,21,20.9,20.8,21,20.6,20.4,20.3,20.3,20.5,20.3,20.5,20.3,20.9,19.6,19,19.2,19.3,19.1,19.8,20.2,20.7,20.7,19.9,19.8,20.3,20.9,20.9,21.7,22.2,22.4,22.3,22,22.2,22.2,22.4,22.5,22.6,23.1,22.8,22.9,23.1,22.9,22.4,22.6,22.6,23.1,23,23.4,23.1,22.9,22.8,22.7,23,23.3,23.6,23.5,23.7,23.3,23.2,23.3,23.2,23.2,23.4,23.3,23.2,23.3,23.6,23.8,24.2,24,23.8,23.7,24,23.8,23.4,23.6,23.7,24,23.9,23.7,23.8,24.2,24.3,24.3,24.4,24.4,24.6,24.3,24.7,24.6,24.9,23.4,23.2,23.5,23.5,23.5,23.8,24.4,24.5,24.6,24.7,24.9,24.9,24.6,24.5,24.7,24.3,24.9,25.4,25,25.2,24.7,24.5,24.6,25.8,25.9,25.7,24.1,23.9,23.2,23.2,24.9,24.9,25.2,24.4,24.2]

#PORTFOLIO INPUT
amt_vnm = 0
amt_hpg = 0
amt_vnd = 200
amt_ssi = 100
amt_cash = 20000

#PORTFOLIO VALUE HISTORY
portfolio = []
for i in range(0,len(vnm)):
    portfolio_instance=vnm[i]*amt_vnm + hpg[i]*amt_hpg +vnd[i]*amt_vnd +ssi[i]*amt_ssi + amt_cash
    portfolio.append(portfolio_instance)

#GET WEIGHTT
value_portfolio = amt_vnm*vnm[0] + amt_hpg*hpg[0] + amt_vnd*vnd[0] + amt_ssi*ssi[0] + amt_cash 
weight_vnm = amt_vnm*vnm[0]/value_portfolio
weight_hpg = amt_hpg*hpg[0]/value_portfolio
weight_vnd = amt_vnd*vnd[0]/value_portfolio
weight_ssi = amt_ssi*ssi[0]/value_portfolio
weight_cash = amt_cash/value_portfolio


#GET RETURN
def get_expectedreturn (returns):
    period = math.ceil(len(returns)/12)
    average_end = sum(returns [0:period]) /period
    average_begin = sum(returns[len(returns)-period:len(returns)-1]) / period
    return_s = (average_end - average_begin)/average_begin
    return return_s

return_portfolio = get_expectedreturn(vnm)*weight_vnm + get_expectedreturn(hpg)*weight_hpg + get_expectedreturn(vnd)*weight_vnd + get_expectedreturn(ssi)*weight_ssi  

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
    return np.cov(get_performance(vnindex),get_performance(x))[1][0]/np.var(get_performance(vnindex))

beta_portfolio = get_beta(vnm)*weight_vnm + get_beta(hpg)*weight_hpg + get_beta(vnd)*weight_vnd + get_beta(ssi)*weight_ssi


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


return_portfolio
var_portfolio
beta_portfolio
maxdd_portfolio















