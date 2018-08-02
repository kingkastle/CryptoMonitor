from coinmarketcap import Market
import pandas as pd


class Coins(object):
    def __init__(self):
        self.coinmarketcap = Market()
        self.current_reference = 'BTC'

    def _parseresponse(self, response):
        result = []
        for coin in response['data'].keys():
            res_coin = {}
            for field, val in response['data'][coin].items():
                if isinstance(val, dict):
                    for currency in response['data'][coin][field].keys():
                        res_coin.update({x + '_' + currency: y for x, y in response['data'][coin][field][currency].items()})
                else:
                    res_coin[field] = val
            result.append(res_coin)
        return result

    def get_coins_summary(self, start=0, limit=100):
        raw_data = self.coinmarketcap.ticker(start=start, limit=limit, convert=self.current_reference)
        data = pd.DataFrame(self._parseresponse(raw_data))
        data['DATETIME'] = pd.to_datetime('today').strftime("%Y-%m-%d")
        return data

