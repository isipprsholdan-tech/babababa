import random
import math
import sys
from VD_games.engine import play_game


DESCRIPTION = 'Найди наибольший общий делитель чисел.'


def generate_round():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)

    question = f"{num1} {num2}"
    correct_answer = math.gcd(num1, num2)

    return question, correct_answer


def main():
    play_game(sys.modules[__name__])


if __name__ == "__main__":
    main()
