import random
import math

def welcome_user():
    print("Welcome to the VD-games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name

def find_gcd(a, b):
    return math.gcd(a, b)

def play_gcd():
    name = welcome_user()
    print('Найди наибольший общий делитель чисел.')

    correct_answers = 0
    rounds_to_win = 3

    while correct_answers < rounds_to_win:
        num1 = random.randint(1, 30)
        num2 = random.randint(1, 30)
        print(f'Вопрос: {num1} {num2}')
        answer = input('Твой ответ: ').strip()

        try:
            user_answer = int(answer)
            correct_answer = find_gcd(num1, num2)

            if user_answer == correct_answer:
                print('Верно!')
                correct_answers += 1
            else:
                print(f"'{answer}' - неверно. Правильный ответ: '{correct_answer}'.")
                print(f'Попробуй ещё раз, {name}!')
                return
        except ValueError:
            print(f"'{answer}' - неверно. Нужно ввести число.")
            print(f'Попробуй ещё раз, {name}!')
            return

    print(f'Поздравляю, {name}!')

def main():
    play_gcd()

if __name__ == '__main__':
    main()
