import random
from brain_games.cli import welcome_user


def is_even(number):
    """Проверка, чётное ли число."""
    return number % 2 == 0


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    name = welcome_user()  # вернёт имя пользователя

    rounds = 3
    for _ in range(rounds):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()

        correct_answer = "yes" if is_even(number) else "no"

        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            return

        print("Correct!")

    print(f"Congratulations, {name}!")

