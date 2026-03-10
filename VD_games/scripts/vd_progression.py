import random
import sys
from VD_games.engine import play_game


DESCRIPTION = 'Какое число пропущено в прогрессии?'


def generate_progression():
    start = random.randint(1, 20)
    step = random.randint(2, 5)
    length = random.randint(5, 10)

    progression = [str(start + i * step) for i in range(length)]

    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."

    return " ".join(progression), correct_answer


def generate_round():
    return generate_progression()


def main():
    play_game(sys.modules[__name__])


if __name__ == "__main__":
    main()
