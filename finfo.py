import requests
import os
import pickle
from time import sleep

class FileCache():
    """
    Support caching in both file and memory
        self.cache[symbol] = res['close']
    """

    def __init__(self, folder):
        self.folder = folder

    def _create_if_not_exists(self, folder):
        if not os.path.exists(folder):
            os.makedirs(folder)

    def store(self, key, value):
        self._create_if_not_exists(self.folder)
        with open(self.folder + '/' + key, 'wb') as f:
            f.write(pickle.dumps(value))

    def get(self, key):
        if os.path.exists(self.folder + '/' + key):
            with open(self.folder + '/' + key, 'rb') as f:
                return pickle.loads(f.read())
        return None

class FinfoAPI():
    URL = 'https://finfo-api.vndirect.com.vn/tradingView/history?symbol={0}'
    STOCK_URL = 'https://finfo-api.vndirect.com.vn/stocks'

    def retrieve(self, symbol):
        """
        Return history price in the latest first fashion
        """
        url = self.URL.format(symbol)
        data = requests.get(url).json()
        res = list(reversed(data['c']))
        sleep(0.1)  # avoid maximum retries exceeded
        return {
            'close': res
        }

    def retrieve_symbol_list(self):
        """
        Return list of all symbols
        """
        data = requests.get(self.STOCK_URL).json()
        return map(lambda x: x['symbol'], data['data'])

class PriceStash():
    """
    Similar to FinfoAPI, but support:

    - Only close price
    - Caching (both in mem and in file)
    - Personal normalize history duration
        (since each symbol has different history duration)
    """
    def __init__(self):
        self.finfo_api = FinfoAPI()
        self.cache = FileCache('temp')

    def full_refetch(self):
        """
        Fully re-fetch all symbol data then cache
        Useful to prepare for demo, but take a long time to run.
        """
        print('Loading symbol list')
        symbols = self.finfo_api.retrieve_symbol_list()
        symbols.append('VNINDEX')
        for s in symbols:
            print('Loading symbol', s)
            self.cache.store(s, self.fetch(s))

    def fetch(self, symbol):
        """
        Similar to get, but does not care about the cache
        """
        res = self.finfo_api.retrieve(symbol)
        self.cache.store(symbol, res['close'])
        return res['close']

    def get(self, symbol):
        """
        By default, after each call the data will be cached
        """
        if self.cache.get(symbol):
            return self.cache.get(symbol)
        return self.fetch(symbol)

    def build_stash(self, symbols):
        """
        Similar to get(symbol), but support trimming history of all symbols to the same length
        Return a dict
        """
        res = {}
        max_length = 250
        for symbol in symbols:
            res[symbol] = self.get(symbol)
            if max_length > len(res[symbol]):
                max_length = len(res[symbol])
        for symbol in symbols:
            res[symbol] = res[symbol][:max_length]
        res['VNINDEX'] = self.get('VNINDEX')[:max_length]
        return res

if __name__ == '__main__':
    """
    Run directly will
    """
    price_stash = PriceStash()
    price_stash.full_refetch()
