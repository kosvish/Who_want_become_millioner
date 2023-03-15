import random

questions = [
    {
        "question": "Какое число является основанием для десятичной системы",
        "answers": ["2", "8", "10", "16"],
        "correct_answer": "10"
    },
    {
        "question": "Какой газ является основным компонентом воздуха?",
        "answers": ["азот", 'кислород', "углекислый газ", "аргон"],
        "correct_answer": "азот"
    },
    {
        "question": "Что из перечисленного является нечетным числом?",
        "answers": ["2", "4", "6", "7"],
        "correct_answer": "7"
    }
]


def ask_question(question, answers):
    print(question)

    for i, answer in enumerate(answers):
        print(f'{i + 1}. {answer}')

    while True:
        user_answer = input("Ваш ответ: ")
        if user_answer.isdigit() and int(user_answer) in range(1, len(answers) + 1):
            return answers[int(user_answer) - 1]


print(f"""
Привествую всех в игре кто хочет стать миллионером!
Суть игры проста у нас есть {len(questions)} вопроса 
Игроку лишь нужно ответь на все них правильно!
За каждый правильный ответ игрок получает 100$
""")


def play_game(questions):
    random.shuffle(questions)

    score = 0
    current_question = 0

    while current_question < len(questions) and ask_question(questions[current_question]["question"],
                                                             questions[current_question]["answers"]) == \
            questions[current_question]["correct_answer"]:
        print("Правильно!")
        score += 1000
        current_question += 1
    else:
        if current_question == len(questions):
            print(f'У нас есть победитель! Он забирает {score}$')
        else:
            print(f'А вот и нет! К сожалению ты потерял все деньги(')


play_game(questions)
