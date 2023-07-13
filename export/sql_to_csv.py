import sqlite3
import csv

# Устанавливаем соединение с базой данных SQLite
conn = sqlite3.connect('../bd/bd.sqlite3')
cursor = conn.cursor()

# Выполняем запрос к базе данных и получаем данные
cursor.execute("SELECT * FROM products")
data = cursor.fetchall()

# Открываем CSV файл для записи
with open('../bd/bd.csv', 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Записываем заголовки столбцов
    csvwriter.writerow(['article', 'barkod', 'name', 'zakup_price', 'ostatok', 'price', 'discount', 'real_price'])
    # Записываем данные
    csvwriter.writerows(data)

# Закрываем соединение с базой данных
conn.close()
