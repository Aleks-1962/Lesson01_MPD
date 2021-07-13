""" Изучить список открытых API. Найти среди них любое, требующее авторизацию (любого типа).
Выполнить запросы к нему, пройдя авторизацию.
Ответ сервера записать в файл."""

import requests
import json


url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
token = '57EUE5KLL2XOXBJV'

headers = {'Content-Type': 'application/json', 'Authorization': token}

response = requests.get(url=url, headers=headers)
response_dat = response.json()
print(response_dat)

with open('data.json', 'w') as outfile:
    json.dump(response_dat, outfile, indent=4)
