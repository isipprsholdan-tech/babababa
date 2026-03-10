import prompt


def welcome_user():
    print("Добро пожаловать в VD Games!")
    name = prompt.string('Как вас зовут? ')
    print(f"Привет, {name}!")
    return name


def play_game(game_module):
    name = welcome_user()
    print(game_module.DESCRIPTION)

    correct_answers = 0
    ROUNDS_TO_WIN = 3

    while correct_answers < ROUNDS_TO_WIN:
        question, correct_answer = game_module.generate_round()

        print(f"Вопрос: {question}")
        user_answer = input("Ваш ответ: ").strip()

        if str(user_answer).lower() == str(correct_answer).lower():
            print("Правильно!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' - неправильный ответ ;(. Правильный ответ: '{correct_answer}'.")
            print(f"Попробуй ещё раз, {name}!")
            return

    print(f"Поздравляю, {name}! Ты выиграл!")
