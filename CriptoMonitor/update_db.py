import pandas as pd
from coin_lists import Coins
from retrive_data import DataRetrieval
from manage_db import ManageDB

# get coin info:
coin_info = Coins()
coin = coin_info.get_coins_summary()
coin_symbols = list(coin.symbol.unique())

# get historical data for coin_symbols:
data_access = DataRetrieval()

# load db:
coinsDB = ManageDB()

# update daily stats:
dailyDB = coinsDB.load_db(coinsDB.path_daily_data)
for coin in coin_symbols:
    if coin == 'BTC':
        data_access.current_reference = 'USD'
        data_access.exchange = 'Coinbase'
    else:
        data_access.current_reference = 'BTC'
        data_access.exchange = 'Binance'
    dy_data = data_access.daily_price_historical(coin)
    if dy_data.shape[0] != 0:
        dailyDB = coinsDB.update_db(dailyDB, dy_data)
    print(coin, dy_data.shape, dailyDB.shape)


coinsDB.save_db(dailyDB, coinsDB.path_daily_data)




