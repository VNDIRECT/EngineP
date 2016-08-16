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


import numpy as np
import matplotlib.pyplot as plt
import cvxopt as opt
from cvxopt import blas, solvers
import pandas as pd
import mpld3
from mpld3 import plugins
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


# Turn off progress printing 
solvers.options['show_progress'] = False

## NUMBER OF ASSETS
#n_assets = 4

## NUMBER OF OBSERVATIONS
#n_obs = 1000  #original 1000

#results in a n_assets x n_obs vector, with a return for each asset in each observed period
#return_vec = np.random.randn(n_assets, n_obs) 
return_vec = np.row_stack((vnm, hpg, vnd, ssi))

## Additional code demonstrating the formation of a Markowitz Bullet from random portfolios:

def rand_weights(n):
    ''' Produces n random weights that sum to 1 '''
    k = np.random.rand(n)
    return k / sum(k)


def random_portfolio(returns):
    ''' 
    Returns the mean and standard deviation of returns for a random portfolio
    '''

    p = np.asmatrix(np.mean(returns, axis=1))
    w = np.asmatrix(rand_weights(returns.shape[0]))
    C = np.asmatrix(np.cov(returns))
    
    mu = w * p.T
    sigma = np.sqrt(w * C * w.T)
    
    # This recursion reduces outliers to keep plots pretty
    if sigma > 2:
        return random_portfolio(returns)
    return mu, sigma


def convert_portfolios(portfolios):
    ''' Takes in a cvxopt matrix of portfolios, returns list '''
    port_list = []
    for portfolio in portfolios:
        temp = np.array(portfolio).T
        port_list.append(temp[0].tolist())
        
    return port_list


def optimal_portfolio(returns):
    ''' returns an optimal portfolio given a matrix of returns '''
    n = len(returns)
    #print n  # n=4, number of assets
    returns = np.asmatrix(returns)
    
    N = 100
    mus = [10**(5.0 * t/N - 1.0) for t in range(N)]
    
    # Convert to cvxopt matrices
    S = opt.matrix(np.cov(returns))  #S is the covariance matrix. diagonal is the variance of each stock

    
    pbar = opt.matrix(np.mean(returns, axis=1))
    print ("pbar:", pbar)

    # Create constraint matrices
    G = -opt.matrix(np.eye(n))   # negative n x n identity matrix
    h = opt.matrix(0.0, (n ,1))
    A = opt.matrix(1.0, (1, n))
    b = opt.matrix(1.0)
    
    # Calculate efficient frontier weights using quadratic programming
    portfolios = [solvers.qp(mu*S, -pbar, G, h, A, b)['x'] 
                  for mu in mus]

    port_list = convert_portfolios(portfolios)
 
   
    ## CALCULATE RISKS AND RETURNS FOR FRONTIER
    returns = [blas.dot(pbar, x) for x in portfolios]  #Different than input returns
    risks = [np.sqrt(blas.dot(x, S*x)) for x in portfolios] #np.sqrt returns the stdev, not variance
    
    ## CALCULATE THE 2ND DEGREE POLYNOMIAL OF THE FRONTIER CURVE
    m1 = np.polyfit(returns, risks, 2)
    #print m1 # result: [ 159.38531535   -3.32476303    0.4910851 ]
    x1 = np.sqrt(m1[2] / m1[0])
    # CALCULATE THE OPTIMAL PORTFOLIO
    wt = solvers.qp(opt.matrix(x1 * S), -pbar, G, h, A, b)['x'] #Is this the tangency portfolio? X1 = slope from origin?  
    print ("wt, optimal portfolio:", wt)
    return np.asarray(wt), returns, risks, port_list



def covmean_portfolio(covariances, mean_returns):
    ''' returns an optimal portfolio given a covariance matrix and matrix of mean returns '''
    n = len(mean_returns)
    
    N = 100
    mus = [10**(5.0 * t/N - 1.0) for t in range(N)]

    S = opt.matrix(covariances)  # how to convert array to matrix?  

    pbar = opt.matrix(mean_returns)  # how to convert array to matrix?

    # Create constraint matrices
    G = -opt.matrix(np.eye(n))   # negative n x n identity matrix
    h = opt.matrix(0.0, (n ,1))
    A = opt.matrix(1.0, (1, n))
    b = opt.matrix(1.0)
    
    # Calculate efficient frontier weights using quadratic programming
    portfolios = [solvers.qp(mu*S, -pbar, G, h, A, b)['x'] 
                  for mu in mus]
    port_list = convert_portfolios(portfolios)
    
    ## CALCULATE RISKS AND RETURNS FOR FRONTIER
    frontier_returns = [blas.dot(pbar, x) for x in portfolios]  
    risks = [np.sqrt(blas.dot(x, S*x)) for x in portfolios] 
    
    ## CALCULATE THE 2ND DEGREE POLYNOMIAL OF THE FRONTIER CURVE
    m1 = np.polyfit(frontier_returns, risks, 2)
    #print m1 # result: [ 159.38531535   -3.32476303    0.4910851 ]
    x1 = np.sqrt(m1[2] / m1[0])
    # CALCULATE THE OPTIMAL PORTFOLIO
    wt = solvers.qp(opt.matrix(x1 * S), -pbar, G, h, A, b)['x']  

    return np.asarray(wt), frontier_returns, risks, port_list


## Example Input from Estimates

covariances = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]] # inner lists represent columns, diagonal is variance
 

mean_returns = [1.5,3.0,5.0,2.5] # Returns in DALYs

weights, returns, risks, portfolios = covmean_portfolio(covariances, mean_returns)
































