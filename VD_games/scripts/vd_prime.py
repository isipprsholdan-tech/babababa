import random
import sys
from VD_games.engine import play_game


DESCRIPTION = 'Ответь "yes", если число простое, иначе "no".'


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def generate_round():
    number = random.randint(1, 100)
    correct_answer = "yes" if is_prime(number) else "no"
    return number, correct_answer


def main():
    play_game(sys.modules[__name__])


if __name__ == "__main__":
    main()
