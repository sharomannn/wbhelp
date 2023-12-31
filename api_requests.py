import requests
from apikey import headers
import json


def wb_prise():
    url = 'https://suppliers-api.wildberries.ru/public/api/v1/info'
    response_price = requests.get(url, headers=headers).json()
    return response_price


def update_wb_prise(items):
    # Отправка запроса к API Wildberries
    url = 'https://suppliers-api.wildberries.ru/public/api/v1/prices'
    response = requests.post(url, headers=headers, data=json.dumps(items, ensure_ascii=False))

    res = response.json()
    print(res)

def update_wb_discont(items):
    print(items)
    # Отправка запроса к API Wildberries
    url = 'https://suppliers-api.wildberries.ru/public/api/v1/updateDiscounts'
    response = requests.post(url, headers=headers, data=json.dumps(items, ensure_ascii=False))

    res = response.json()
    print(res)