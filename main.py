import sqlite3
from api_requests import wb_prise, update_wb_prise


def main():
    # Установка скидки
    discount(45)

    # Перерасчёт реальных цен
    updete_realprise()

    # Выгрузка цен с ВБ
    # updete_price_discont(wb_prise)

    update_wb_prise(post_item_wb_price)


def post_item_wb_price():
    conn = sqlite3.connect('bd/bd.sqlite3')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    prods = cursor.fetchall()

    items = []
    for prod in prods:
        items.append({
            'nmId': int(prod[1]),
            'price': round(prod[7])
        })
    items = items[0:2]

    return items



def updete_realprise():
    conn = sqlite3.connect('bd/bd.sqlite3')
    cursor = conn.cursor()
    # Увеличение цены
    # cursor.execute("UPDATE products SET price = price + (price * 25 / 100)")
    # Обновление реальной цены
    cursor.execute("UPDATE products SET real_price = price - (price * discount / 100)")

    conn.commit()
    conn.close()


# Добавляем данные по скидкам в БД
def updete_price_discont(response):
    conn = sqlite3.connect('bd/bd.sqlite3')
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
    conn = sqlite3.connect('bd/bd.sqlite3')
    cursor = conn.cursor()

    # Обновляем данные в столбце 'discount'
    new_discount = number  # Новое значение скидки
    cursor.execute("UPDATE products SET discount = ?", (new_discount,))

    # Фиксируем изменения и закрываем соединение с базой данных
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
