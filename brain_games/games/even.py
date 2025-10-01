import random

MIN_NUMBER = 1
MAX_NUMBER = 100

TASK = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_round():
    number = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = str(number)
    correct_answer = "yes" if is_even(number) else "no"
    return question, correct_answer

