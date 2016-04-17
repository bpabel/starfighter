
from os.path import join, dirname, abspath, normpath

import requests
import json


class API(object):

    def __init__(self, account=None, api_key=None):
        super(API, self).__init__()
        self.account = account
        if api_key is None:
            fp = normpath(join(abspath(__file__), '../data/api_key.txt'))
            with open(fp, 'r') as f:
                api_key = f.read().strip()
        self.api_key = api_key

    def heartbeat(self, timeout=1):
        url = r'https://api.stockfighter.io/ob/api/heartbeat'
        try:
            r = requests.get(url, timeout=timeout)
        except requests.Timeout:
            return False
        else:
            return r.status_code == 200 and r.json()['ok']

    def venue_heartbeat(self, venue, timeout=1):
        url = 'https://api.stockfighter.io/ob/api/venues/{venue}/heartbeat'.format(venue=venue)
        try:
            r = requests.get(url, timeout=timeout)
        except requests.Timeout:
            return False
        else:
            return r.status_code == 200 and r.json()['ok']

    def stocks(self, venue, timeout=1):
        url = r'https://api.stockfighter.io/ob/api/venues/{venue}/stocks'.format(venue=venue)
        r = requests.get(url, timeout=timeout)
        return r.json()['symbols']

    def orderbook(self, venue, stock):
        url = r'https://api.stockfighter.io/ob/api/venues/{venue}/stocks/{stock}'.format(venue=venue, stock=stock)
        r = requests.get(url, timeout=10)
        return r.json()

    def order(self, venue, stock, price, qty, direction, ordertype):
        url = r'https://api.stockfighter.io/ob/api/venues/{venue}/stocks/{stock}/orders'.format(venue=venue, stock=stock)
        headers = {'X-Starfighter-Authorization': self.api_key}
        data = {
            "account": self.account,
            "venue": venue,
            "stock": stock,
            'price': price,
            "qty": qty,
            "direction": direction,
            "orderType": ordertype,
        }
        r = requests.post(url, data=json.dumps(data), headers=headers)
        return r.json()
