import requests
import pandas as pd
import ast
import time

def historical_daily_data(productID):

    url = "https://api.exchange.coinbase.com/products/" + productID + "/candles?granularity=86400"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    tmp = pd.DataFrame(ast.literal_eval(response.text), columns=['date', 'open', 'high', 'low', 'close', 'volume'])
    tmp['date'] = tmp['date'].apply(lambda x: time.strftime("%Y-%m-%d", time.localtime(x)))
    tmp = tmp.set_index('date')
    return(tmp)

eth = historical_daily_data("ETH-USD")
