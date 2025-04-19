import sqlite3

# 1. Создание базы данных и подключение к ней
conn = sqlite3.connect("hw.db")
cursor = conn.cursor()

# 2-6. Создание таблицы products с нужными полями
cursor.execute('''
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT NOT NULL CHECK(LENGTH(product_title) <= 200),
    price REAL NOT NULL DEFAULT 0.0,
    quantity INTEGER NOT NULL DEFAULT 0
)
''')
conn.commit()

# 7. Добавление 15 различных товаров
def insert_sample_products():
    products = [
        ("Мыло детское", 45.5, 10),
        ("Жидкое мыло с запахом ванили", 89.9, 7),
        ("Зубная паста", 120.0, 3),
        ("Шампунь", 150.0, 5),
        ("Бумага туалетная", 35.0, 25),
        ("Салфетки влажные", 60.0, 12),
        ("Стиральный порошок", 250.0, 4),
        ("Гель для душа", 110.0, 6),
        ("Щетка зубная", 75.0, 15),
        ("Освежитель воздуха", 95.0, 8),
        ("Мыло хозяйственное", 40.0, 20),
        ("Пена для бритья", 130.0, 2),
        ("Бальзам для волос", 145.0, 3),
        ("Крем для рук", 85.0, 9),
        ("Средство для мытья посуды", 99.0, 10)
    ]
    cursor.executemany('''
        INSERT INTO products (product_title, price, quantity)
        VALUES (?, ?, ?)
    ''', products)
    conn.commit()

# 8. Обновление количества товара по id
def update_quantity(product_id, new_quantity):
    cursor.execute('''
        UPDATE products SET quantity = ? WHERE id = ?
    ''', (new_quantity, product_id))
    conn.commit()

# 9. Обновление цены товара по id
def update_price(product_id, new_price):
    cursor.execute('''
        UPDATE products SET price = ? WHERE id = ?
    ''', (new_price, product_id))
    conn.commit()

# 10. Удаление товара по id
def delete_product(product_id):
    cursor.execute('''
        DELETE FROM products WHERE id = ?
    ''', (product_id,))
    conn.commit()

# 11. Вывод всех товаров
def print_all_products():
    cursor.execute('SELECT * FROM products')
    for row in cursor.fetchall():
        print(row)

# 12. Поиск товаров дешевле лимита по цене и с количеством больше лимита
def filter_products_by_price_and_quantity(price_limit, quantity_limit):
    cursor.execute('''
        SELECT * FROM products
        WHERE price < ? AND quantity > ?
    ''', (price_limit, quantity_limit))
    for row in cursor.fetchall():
        print(row)

# 13. Поиск товаров по названию
def search_products_by_title(keyword):
    cursor.execute('''
        SELECT * FROM products
        WHERE product_title LIKE ?
    ''', (f'%{keyword}%',))
    for row in cursor.fetchall():
        print(row)

# 14. Тестирование функций
def test_all_functions():
    print("Вставка 15 товаров:")
    insert_sample_products()
    print_all_products()

    print("\nОбновление количества (id=1, new_quantity=20):")
    update_quantity(1, 20)
    print_all_products()

    print("\nОбновление цены (id=2, new_price=55.5):")
    update_price(2, 55.5)
    print_all_products()

    print("\nУдаление товара (id=3):")
    delete_product(3)
    print_all_products()

    print("\nФильтр по цене < 100 и количеству > 5:")
    filter_products_by_price_and_quantity(100, 5)

    print("\nПоиск по слову 'мыло':")
    search_products_by_title("мыло")

# Выполнить тесты
if __name__ == "__main__":
    test_all_functions()

# Закрытие соединения
conn.close()
