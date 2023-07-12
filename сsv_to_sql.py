import sqlite3
import csv

# Устанавливаем соединение с базой данных SQLite
conn = sqlite3.connect('bd.sqlite3')
cursor = conn.cursor()

# Создаем таблицу в базе данных
cursor.execute('''CREATE TABLE IF NOT EXISTS products (
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
with open('bd.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    next(csvreader)  # Пропускаем заголовок CSV файла
    for row in csvreader:
        cursor.execute("INSERT INTO products (article, barkod, name, zakup_price, ostatok, price, discount, real_price) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       (row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))

# Фиксируем изменения и закрываем соединение с базой данных
conn.commit()
conn.close()
