import random

MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_START = 1
MAX_START = 20
MIN_STEP = 1
MAX_STEP = 10
HIDDEN_PLACEHOLDER = ".."

TASK = "What number is missing in the progression?"


def make_progression(start, step, length):
    return [start + i * step for i in range(length)]


def get_round():
    length = random.randint(MIN_LENGTH, MAX_LENGTH)
    start = random.randint(MIN_START, MAX_START)
    step = random.randint(MIN_STEP, MAX_STEP)

    progression = make_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)

    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = HIDDEN_PLACEHOLDER
    question = " ".join(map(str, progression))

    return question, correct_answer

