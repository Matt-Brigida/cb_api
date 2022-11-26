import requests
import pandas as pd

def historical_daily_data(productID, frequency):

    url = "https://api.exchange.coinbase.com/products/" + productID + "/candles?granularity=8600"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    print(response.text)