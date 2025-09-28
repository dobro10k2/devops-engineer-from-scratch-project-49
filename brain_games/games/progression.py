import random

TASK = "What number is missing in the progression?"


def make_progression(start, step, length):
    """Создаёт арифметическую прогрессию заданной длины."""
    return [start + i * step for i in range(length)]


def get_round():
    length = random.randint(5, 10)  # длина от 5 до 10 включительно
    start = random.randint(1, 20)
    step = random.randint(1, 10)

    progression = make_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)

    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))

    return question, correct_answer

