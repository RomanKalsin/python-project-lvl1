# Просим пользователя ввести имя, возвращаем имя
import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    return name
