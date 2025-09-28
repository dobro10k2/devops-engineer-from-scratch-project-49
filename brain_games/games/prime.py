import random

TASK = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def get_round():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"
    return question, correct_answer

