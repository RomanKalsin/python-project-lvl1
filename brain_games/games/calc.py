from random import randint, choice
from prompt import integer


tutorial = "What is the result of the expression?"


def game():
    num1 = randint(0, 100)
    num2 = randint(0, 100)
    symbol = choice(["+", "-", "*"])
    if symbol == "+":
        result = num1 + num2
        print("Question: {} {} {}".format(num1, symbol, num2))
        ansver = integer("Your answer: ")
        is_correct = True if result == ansver else False
    elif symbol == "-":
        result = num1 - num2
        print("Question: {} {} {}".format(num1, symbol, num2))
        ansver = integer("Your answer: ")
        is_correct = True if result == ansver else False
    elif symbol == "*":
        result = num1 * num2
        print("Question: {} {} {}".format(num1, symbol, num2))
        ansver = integer("Your answer: ")
        is_correct = True if result == ansver else False
    return is_correct, ansver, result
