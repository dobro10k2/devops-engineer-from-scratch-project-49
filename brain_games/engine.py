from brain_games.cli import welcome_user

ROUNDS_COUNT = 3


def run_game(game):
    name = welcome_user()
    print(game.TASK)

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game.get_round()
        print(f"Question: {question}")
        answer = input("Your answer: ")

        if answer != correct_answer:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )            
            print(f"Let's try again, {name}!")
            return

        print("Correct!")

    print(f"Congratulations, {name}!")

