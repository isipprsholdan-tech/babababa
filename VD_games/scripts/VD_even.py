import random

def is_even(number):
    return number % 2 == 0

def play_game():
    print("Welcome to the VD-games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    QUESTIONS_COUNT = 3

    while correct_answers < QUESTIONS_COUNT:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()

        if is_even(number):
            correct = "yes"
        else:
            correct = "no"

        if answer == correct:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")

def main():
    play_game()

if __name__ == "__main__":
    main()
