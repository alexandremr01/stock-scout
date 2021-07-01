ALPHAV_API_KEY = 'RFDULN6WICNLKGDL'
ALPHAV_BASE_URL = 'https://www.alphavantage.co/query?'

HGBR_API_KEY = '07200053'
HGBR_BASE_URL = 'https://api.hgbrasil.com/finance'

import requests

def alpha_vantage_client(sym, freq):
    alphav = {
        'DAY': 'TIME_SERIES_DAILY_ADJUSTED',
        'WEEK': 'TIME_SERIES_WEEKLY_ADJUSTED',
        'MONTH': 'TIME_SERIES_MONTHLY_ADJUSTED'
    }

    response = requests.get(f'{ALPHAV_BASE_URL}function={alphav[freq]}&symbol={sym}&apikey={ALPHAV_API_KEY}')
    return response.json()

def hg_brasil_client():
    response = requests.get(f'{HGBR_BASE_URL}?key={HGBR_API_KEY}')
    return response.json()
