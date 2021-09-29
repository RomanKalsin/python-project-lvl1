from random import randint
from prompt import string


tutorial = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
    num = randint(1, 100)
    print("Question: {}".format(num))
    reuslt = is_prime(num)
    ansver = string("Your answer: ")
    is_correct = True if ansver.lower() == reuslt else False
    return is_correct, ansver, reuslt


def is_prime(num):
    i = num
    while i > 2:
        i -= 1
        if num % i == 0:
            return "no"
    return "yes"
