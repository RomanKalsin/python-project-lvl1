#!/usr/bin/env/ python3


from brain_games.welcome import welcome
from random import randint
import prompt


def main():
    name = welcome()
    brain_even(name)


def brain_even(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        num = randint(1, 100)
        print("Question: {}".format(num))
        correct = ""
        ansver = prompt.string("Your answer: ")
        correct = "yes" if num % 2 == 0 else "no"
        if correct != ansver.lower():
            print("'{}' is wrong answer ;(. Correct answer was '{}'. "
                  "\n Let's try again, {}!".format(ansver, correct, name))
            break
        print("Correct!")
        i += 1
    else:
        print("Congratulations, {}!".format(name))
