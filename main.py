import sqlite3
import streamlit as st

from api_requests import wb_prise, update_wb_prise, update_wb_discont

conn = sqlite3.connect("bd/bd.sqlite3")
cursor = conn.cursor()


def main():
    result = st.button('Обновить скидку')
    age = st.slider('Укажите скидку:', 0, 100, 45)

    data_container = st.empty()  # Создаем пустой контейнер
    data = query_data()

    data_container.dataframe(data,
                            column_config = {
                                "1": st.column_config.NumberColumn("ID WB", format='%i'),
                                "2": st.column_config.Column("Артикул"),
                                "3": st.column_config.Column("Баркод"),
                                "4": st.column_config.Column("Название"),
                                "5": st.column_config.Column("Закупочная цена"),
                                "6": st.column_config.Column("Остаток"),
                                "7": st.column_config.Column("Цена без скидки"),
                                "8": st.column_config.Column("Скидка"),
                                "9": st.column_config.Column("Реальная цена")
                            }
                             )
    if result:
        discount(age)
        st.experimental_rerun()

    # Установка скидки
    # discount(55)

    # # Перерасчёт реальных цен
    # updete_realprise()

    # Выгрузка цен с ВБ
    # updete_price_discont(wb_prise())

    # Обновление цены на ВБ
    # update_wb_prise(post_item_wb_price())

    # update_wb_discont(post_item_wb_discont())


def query_data():
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    conn.close()
    return data


def post_item_wb_discont():
    conn = sqlite3.connect('bd/bd.sqlite3')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")
    prods = cursor.fetchall()

    items = []
    for prod in prods:
        items.append({
            'discount': round(prod[8]),
            'nm': int(prod[1])
        })
    return items


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


def discount(age):
    # Устанавливаем соединение с базой данных SQLite
    conn = sqlite3.connect('bd/bd.sqlite3')
    cursor = conn.cursor()

    # Обновляем данные в столбце 'discount'
    new_discount = age  # Новое значение скидки
    cursor.execute("UPDATE products SET discount = ?", (new_discount,))

    # Фиксируем изменения и закрываем соединение с базой данных
    conn.commit()
    conn.close()


if __name__ == '__main__':
    main()
