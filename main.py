import requests
import sqlite3
import json
from json import loads
from apikey import headers


def main():
    discount(25)
    updete_realprise()

    # url = 'https://suppliers-api.wildberries.ru/public/api/v1/info'
    # # headers = {
    # #     'Authorization': API_TOKEN,
    # #     'Content-Type': 'application/json'
    # # }
    # response = requests.get(url, headers=headers).json()
    # print(response)
    # print(type(response))
    # updete_price_discon(response)


def updete_realprise():
    conn = sqlite3.connect('bd.sqlite3')
    cursor = conn.cursor()
    cursor.execute("UPDATE products SET real_price = price - (price * discount / 100))")

    conn.commit()
    conn.close()


# Добавляем данные по скидкам в БД
def updete_price_discon(response):
    conn = sqlite3.connect('bd.sqlite3')
    cursor = conn.cursor()

    for item in response:
        price = item['price']
        nmID = item['nmId']
        discount = item['discount']
        cursor.execute(f"UPDATE products SET price = {price}, discount = {discount} WHERE id_wb = {nmID}")

    conn.commit()
    conn.close()


def discount(number):
    # Устанавливаем соединение с базой данных SQLite
    conn = sqlite3.connect('bd.sqlite3')
    cursor = conn.cursor()

    # Обновляем данные в столбце 'discount'
    new_discount = number  # Новое значение скидки
    cursor.execute("UPDATE products SET discount = ?", (new_discount,))

    # Фиксируем изменения и закрываем соединение с базой данных
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
