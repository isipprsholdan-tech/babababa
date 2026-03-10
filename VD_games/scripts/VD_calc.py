import random
import sys
from VD_games.engine import play_game


DESCRIPTION = 'Каков результат выражения?'


def calculate(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    else:
        return num1 * num2


def generate_round():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(['+', '-', '*'])

    question = f"{num1} {operation} {num2}"
    correct_answer = calculate(num1, num2, operation)

    return question, correct_answer


def main():
    play_game(sys.modules[__name__])


if __name__ == "__main__":
    main()
