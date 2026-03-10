import random
import sys
from VD_games.engine import play_game


DESCRIPTION = 'Ответь "yes", если число чётное, иначе "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_even(number) else "no"
    return number, correct_answer


def main():
    play_game(sys.modules[__name__])


if __name__ == "__main__":
    main()
