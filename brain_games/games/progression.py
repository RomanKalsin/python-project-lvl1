from random import randint
from prompt import integer


tutorial = "What number is missing in the progression?"


def game():
    progression = make_progression()
    index = randint(0, 9)
    result = progression[index]
    string = "Question: "
    for i in progression:
        if i != result:
            string = string + "{} ".format(str(i))
        else:
            string = string + ".. "
    print(string)
    ansver = integer("Your answer: ")
    is_correct = True if ansver == result else False
    return is_correct, ansver, result


def make_progression():
    start = randint(0, 90)
    step = randint(1, 5)
    progression = [i for i in range(start, start + 10 * step, step)]
    return progression
