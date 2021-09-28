from random import randint
from prompt import integer


tutorial = "Find the greatest common divisor of given numbers."


def game():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    result = gcd(num1, num2)
    print("Question: {} {}".format(num1, num2))
    ansver = integer("Question: ")
    is_correct = True if result == ansver else False
    return is_correct, ansver, result


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x
