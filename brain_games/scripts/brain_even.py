#!/usr/bin/env python3
import prompt
import random
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")

    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0

    while i < 3:
        number = random.randint(1, 50)
        print('Question: ' + str(number))
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        if correct_answer == answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
        i += 1

    print(f'Congratulations, {name}!')


if __name__ == '__main__':
    main()
