import sqlite3
import csv

# Устанавливаем соединение с базой данных SQLite
conn = sqlite3.connect('../bd/bd.sqlite3')
cursor = conn.cursor()

# Создаем таблицу в базе данных
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                    pk INTEGER PRIMARY KEY,
                    id_wb INTEGER,
                    article TEXT,
                    barkod TEXT,
                    name TEXT,
                    zakup_price REAL,
                    ostatok INTEGER,
                    price REAL,
                    discount INTEGER,
                    real_price REAL
                )''')

# Открываем CSV файл и загружаем данные в базу данных
with open('../bd/bd.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Пропускаем заголовок CSV файла
    for row in csvreader:
        cursor.execute("INSERT INTO products (id_wb, article, barkod, name, zakup_price, ostatok, price, discount, real_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

# Фиксируем изменения и закрываем соединение с базой данных
conn.commit()
conn.close()
