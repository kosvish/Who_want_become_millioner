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
        "correct_answer": "10"
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
