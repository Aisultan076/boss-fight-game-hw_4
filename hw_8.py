import sqlite3

# Создаем подключение к базе данных (или файл, если его нет)
conn = sqlite3.connect("school.db")
cursor = conn.cursor()

# 1. Создание таблицы countries
cursor.execute("""
CREATE TABLE IF NOT EXISTS countries (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
);
""")

# 2. Добавление 3 стран
cursor.executemany("INSERT INTO countries (title) VALUES (?);", [
    ('Россия',),
    ('США',),
    ('Германия',)
])

# 3. Создание таблицы cities
cursor.execute("""
CREATE TABLE IF NOT EXISTS cities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    area REAL DEFAULT 0,
    country_id INTEGER,
    FOREIGN KEY (country_id) REFERENCES countries(id)
);
""")

# 4. Добавление 7 городов
cursor.executemany("INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?);", [
    ('Москва', 2561.5, 1),
    ('Санкт-Петербург', 1439, 1),
    ('Нью-Йорк', 783.8, 2),
    ('Лос-Анджелес', 1302, 2),
    ('Берлин', 891.7, 3),
    ('Мюнхен', 310.7, 3),
    ('Казань', 425.3, 1),
])

# 5. Создание таблицы students
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    city_id INTEGER,
    FOREIGN KEY (city_id) REFERENCES cities(id)
);
""")

# 6. Добавление 15 учеников
cursor.executemany("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?);", [
    ('Иван', 'Иванов', 1),
    ('Мария', 'Петрова', 2),
    ('Джон', 'Смит', 3),
    ('Эмили', 'Джонсон', 4),
    ('Фриц', 'Мюллер', 5),
    ('Анна', 'Шнайдер', 6),
    ('Дмитрий', 'Сидоров', 1),
    ('Светлана', 'Кузнецова', 2),
    ('Майкл', 'Браун', 3),
    ('Сара', 'Дэвис', 4),
    ('Ганс', 'Вагнер', 5),
    ('Лена', 'Майер', 6),
    ('Алексей', 'Попов', 7),
    ('Ольга', 'Федорова', 7),
    ('Виктор', 'Ковалев', 1),
])

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()

print("База данных успешно создана и заполнена.")
