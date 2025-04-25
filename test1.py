import sqlite3

def create_database():
    conn = sqlite3.connect("shop.db")
    cursor = conn.cursor()

    # Удаляем таблицы, если они существуют
    cursor.execute("DROP TABLE IF EXISTS products")
    cursor.execute("DROP TABLE IF EXISTS categories")
    cursor.execute("DROP TABLE IF EXISTS stores")

    # Создание таблицы магазинов
    cursor.execute("""
        CREATE TABLE stores (
            store_id INTEGER PRIMARY KEY,
            title VARCHAR(100)
        )
    """)

    # Создание таблицы категорий
    cursor.execute("""
        CREATE TABLE categories (
            code VARCHAR(2) PRIMARY KEY,
            title VARCHAR(150)
        )
    """)

    # Создание таблицы продуктов
    cursor.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            title VARCHAR(250),
            category_code VARCHAR(2),
            unit_price FLOAT,
            stock_quantity INTEGER,
            store_id INTEGER,
            FOREIGN KEY (category_code) REFERENCES categories(code),
            FOREIGN KEY (store_id) REFERENCES stores(store_id)
        )
    """)

    # Заполнение таблицы магазинов
    stores = [
        (1, "Asia"),
        (2, "Globus"),
        (3, "Spar")
    ]
    cursor.executemany("INSERT INTO stores VALUES (?, ?)", stores)

    # Заполнение таблицы категорий
    categories = [
        ("FD", "Food products"),
        ("EL", "Electronics"),
        ("CL", "Clothing")
    ]
    cursor.executemany("INSERT INTO categories VALUES (?, ?)", categories)

    # Заполнение таблицы продуктов
    products = [
        (1, "Chocolate", "FD", 10.5, 129, 1),
        (2, "Apple", "FD", 2.3, 200, 1),
        (3, "TV", "EL", 450.0, 10, 2),
        (4, "T-shirt", "CL", 15.0, 50, 3),
        (5, "Milk", "FD", 1.5, 75, 3),
    ]
    cursor.executemany("INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)", products)

    conn.commit()
    conn.close()
    print("База данных успешно создана и заполнена.")

if __name__ == "__main__":
    create_database()
