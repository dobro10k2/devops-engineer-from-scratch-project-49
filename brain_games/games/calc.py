import random

MIN_NUMBER = 1
MAX_NUMBER = 20
OPERATIONS = ["+", "-", "*"]

TASK = "What is the result of the expression?"


def get_round():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    op = random.choice(OPERATIONS)

    match op:
        case "+":
            correct_answer = num1 + num2
        case "-":
            correct_answer = num1 - num2
        case "*":
            correct_answer = num1 * num2
        case _:
            raise ValueError("Unknown operator")

    question = f"{num1} {op} {num2}"
    return question, str(correct_answer)

