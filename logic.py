import random


def play_game(min_num, max_num, attempts, balance):
    target = random.randint(min_num, max_num)

    print(f"Угадай число от {min_num} до {max_num}. У тебя {attempts} попыток.")

    while attempts > 0 and balance > 0:
        try:
            guess = int(input("Введите число: "))
            bet = int(input(f"Сколько ставите? (текущий баланс: {balance}): "))

            if bet > balance or bet <= 0:
                print("Недопустимая ставка!")
                continue

            attempts -= 1

            if guess == target:
                balance += bet
                print(f"Поздравляем! Вы угадали. Баланс удвоен до {balance}")
                break
            else:
                balance -= bet
                print(f"Неверно! Осталось попыток: {attempts}. Баланс: {balance}")

        except ValueError:
            print("Ошибка ввода. Введите число.")

    print("Игра окончена. Загаданное число было:", target)
    print("Ваш итоговый баланс:", balance)
