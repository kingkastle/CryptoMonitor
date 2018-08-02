import requests
import pandas as pd
import numpy as np
from datetime import datetime
import logging


class DataRetrieval(object):
    def __init__(self):
        self.source = 'https://min-api.cryptocompare.com'
        self.exchange = 'Binance'
        self.current_reference = 'BTC'

    def _retrieve_df(self, coin, url, timeformat="%Y-%m-%d"):
        page = requests.get(url)
        data = page.json()['Data']
        df = pd.DataFrame(data)
        if df.shape[0] == 0:
            logging.info('No data for coin: {0} in current ref: {1}'.format(coin, self.current_reference))
            return df
        df['timestamp'] = [datetime.fromtimestamp(d).strftime(timeformat) for d in df.time]
        df['coin'] = coin
        return df

    def current_price(self, coin):
        url = self.source + '/data/price?fsym={}&tsyms={}' \
            .format(coin.upper(), ','.join([self.current_reference]).upper())
        url += '&e={}'.format(self.exchange)
        page = requests.get(url)
        data = page.json()
        if self.current_reference not in data.keys():
            return np.nan
        return data

    def daily_price_historical(self, coin, limit=10, aggregate=1, allData='true'):
        url = self.source + '/data/histoday?fsym={}&tsym={}&limit={}&aggregate={}&allData={}' \
            .format(coin.upper(), self.current_reference.upper(), limit, aggregate, allData)
        url += '&e={}'.format(self.exchange)
        return self._retrieve_df(coin, url)

    def hourly_price_historical(self, coin, limit, aggregate):
        url = self.source + '/data/histohour?fsym={}&tsym={}&limit={}&aggregate={}' \
            .format(coin.upper(), self.current_reference.upper(), limit, aggregate)
        url += '&e={}'.format(self.exchange)
        return self._retrieve_df(coin, url, timeformat="%Y-%m-%d %H")

    def minute_price_historical(self, coin, limit, aggregate):
        url = self.source + '/data/histominute?fsym={}&tsym={}&limit={}&aggregate={}' \
            .format(coin.upper(), self.current_reference.upper(), limit, aggregate)
        url += '&e={}'.format(self.exchange)
        return self._retrieve_df(coin, url, timeformat="%Y-%m-%d %H-%M")
