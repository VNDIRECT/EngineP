"""
Similar to portfolioopt,

but support out price input
"""
import finfo
import portfolioopt as pfopt
import pandas as pd
import numpy as np

price_stash = finfo.PriceStash()

def markowitz(symbols):
    """
    I can optimize any list of symbol as long as there is a price
    """
    price = price_stash.build_stash(symbols)
    prices = [list(reversed(price.get(s))) for s in symbols]
    arr = np.row_stack(prices)
    return_vec = np.rot90(arr, 3)
    df = pd.DataFrame(return_vec)
    df.columns = list(reversed(symbols))

    returns = (df.shift(-1) - df) / df
    returns = returns.dropna()
    cov_mat = returns.cov()
    avg_rets = returns.mean()
    target_ret = avg_rets.quantile(0.7)

    weights = pfopt.markowitz_portfolio(cov_mat, avg_rets, target_ret)
    return {symbol: weights[symbol] for symbol in symbols}
