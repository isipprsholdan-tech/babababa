import random
import prompt

def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name

def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    else:
        return num1 * num2

def play_calc():
    print("Welcome to the VD-games!")
    name = welcome_user()
    print('Что будет в результате')

    correct_answers = 0
    rounds_to_win = 3

    while correct_answers < rounds_to_win:
        num1 = random.randint(1, 20)
        num2 = random.randint(1, 20)
        operation = random.choice(['+', '-', '*'])

        print(f'Вопрос: {num1} {operation} {num2}')
        answer = input('Ваш ответ: ').strip()

        try:
            user_answer = int(answer)
            correct_answer = calculate(num1, num2, operation)

            if user_answer == correct_answer:
                print('Правильно!')
                correct_answers += 1
            else:
                print(f'{answer} - неправильно. Верный ответ: {correct_answer}')
                print(f'Попробуйте снова, {name}!')
                return
        except ValueError:
            print(f'{answer} - неправильно. Верный ответ: число')
            print(f'Попробуйте снова, {name}!')
            return

    print(f'Поздравляю, {name}! Вы выиграли!')

def main():
    play_calc()

if __name__ == "__main__":
    main()
