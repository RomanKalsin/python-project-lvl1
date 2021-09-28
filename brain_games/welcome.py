# Приветствуем пользователя получем его имя
from prompt import string as input_name


def welcome():
    print("Welcome to the Brain Games!")
    name = input_name("May I have your name? ")
    print('Hello, {}!'.format(name))
    return name
