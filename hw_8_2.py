import sqlite3

def main():
    conn = sqlite3.connect("school.db")
    cursor = conn.cursor()

    while True:
        print("\nВы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

        # Получение и отображение списка городов
        cursor.execute("SELECT id, title FROM cities")
        cities = cursor.fetchall()
        for city in cities:
            print(f"{city[0]}. {city[1]}")

        # Получение ввода от пользователя
        try:
            user_input = int(input("\nВведите id города: "))
        except ValueError:
            print("Пожалуйста, введите корректный числовой id.")
            continue

        if user_input == 0:
            print("Выход из программы.")
            break

        # Поиск учеников по выбранному id города
        cursor.execute("""
            SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
            FROM students
            JOIN cities ON students.city_id = cities.id
            JOIN countries ON cities.country_id = countries.id
            WHERE cities.id = ?
        """, (user_input,))
        students = cursor.fetchall()

        if students:
            print("\nСписок учеников:")
            for student in students:
                print(f"{student[0]} {student[1]} — {student[2]}, город {student[3]} (площадь: {student[4]} км²)")
        else:
            print("В этом городе нет зарегистрированных учеников.")

    conn.close()

if __name__ == "__main__":
    main()
