import random

TASK = "What is the result of the expression?"


def get_round():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op = random.choice(["+", "-", "*"])

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

