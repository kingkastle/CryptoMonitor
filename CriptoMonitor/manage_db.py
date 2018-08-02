import pandas as pd


class ManageDB(object):
    def __init__(self):
        self.path_hourly_data = '/home/osboxes/home/osboxes/bitbot/database/hourly_data.pkl'
        self.path_daily_data = '/home/osboxes/home/osboxes/bitbot/database/daily_data.pkl'

    def load_db(self, path):
        return pd.read_pickle(path)

    def save_db(self, db, path):
        return db.to_pickle(path)

    def update_db(self, db, data):
        return pd.merge(db, data, how='outer')
