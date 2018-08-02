from pytrends.request import TrendReq
import requests

class GTrend(object):
    def __init__(self):
        self.pytrends = TrendReq(hl='en-US', tz=360)

    def get_gtrend(self, coin, period='today 5-y'):
        self.pytrends.build_payload([coin], cat=1138, timeframe=period, geo='', gprop='')
        return self.pytrends.interest_over_time()

    def live_social_status(self, coin, symbol_id_dict={}):
        if not symbol_id_dict:
            symbol_id_dict = {
                'BTC': 1182,
                'ETH': 7605,
                'LTC': 3808
            }
        symbol_id = symbol_id_dict[coin.upper()]
        url = 'https://www.cryptocompare.com/api/data/socialstats/?id={}' \
            .format(symbol_id)
        page = requests.get(url)
        data = page.json()['Data']
        return data
