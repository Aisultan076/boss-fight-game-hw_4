import sqlite3

def connect_db():
    return sqlite3.connect("shop.db")

def get_stores(cursor):
    cursor.execute("SELECT store_id, title FROM stores")
    return cursor.fetchall()

def get_products_by_store(cursor, store_id):
    query = """
        SELECT 
            p.title,
            c.title,
            p.unit_price,
            p.stock_quantity
        FROM products p
        JOIN categories c ON p.category_code = c.code
        WHERE p.store_id = ?
    """
    cursor.execute(query, (store_id,))
    return cursor.fetchall()

def main():
    conn = connect_db()
    cursor = conn.cursor()

    while True:
        print("\nВы можете отобразить список продуктов по выбранному id магазина из")
        print("перечня магазинов ниже, для выхода из программы введите цифру 0:\n")

        stores = get_stores(cursor)
        for store in stores:
            print(f"{store[0]}. {store[1]}")

        try:
            choice = int(input("\nВведите id магазина: "))
        except ValueError:
            print("Пожалуйста, введите корректное число.")
            continue

        if choice == 0:
            print("Выход из программы.")
            break

        store_ids = [store[0] for store in stores]
        if choice not in store_ids:
            print("Магазин с таким id не найден. Попробуйте снова.")
            continue

        products = get_products_by_store(cursor, choice)

        if not products:
            print("В выбранном магазине нет продуктов.")
        else:
            for product in products:
                print(f"\nНазвание продукта: {product[0]}")
                print(f"Категория: {product[1]}")
                print(f"Цена: {product[2]}")
                print(f"Количество на складе: {product[3]}")

    conn.close()

if __name__ == "__main__":
    main()
