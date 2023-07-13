import sqlite3
import requests
from api_requests import wb_prise
from apikey import headers
import json

conn = sqlite3.connect('bd/bd.sqlite3')
cursor = conn.cursor()

# Получение товаров из базы данных
cursor.execute("SELECT * FROM products")
prods = cursor.fetchall()

items = []
for prod in prods:
    items.append({
        'nmId': int(prod[1]),  # Предполагается, что столбец `wb_id` находится на первом месте (индекс 0)
        'price': round(prod[7])  # Предполагается, что столбец `price` находится на втором месте (индекс 1)
    })
items = items[0:2]
print(items)

# Отправка запроса к API Wildberries
url = 'https://suppliers-api.wildberries.ru/public/api/v1/prices'
response = requests.post(url, headers=headers, data=json.dumps(items, ensure_ascii=False))

res = response.json()
print(res)