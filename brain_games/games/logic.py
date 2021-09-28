from brain_games.welcome import welcome


def game_logic(tutorial, game):
    name = welcome()
    print(tutorial)
    i = 0
    while i < 3:
        is_correct, ansver, result = game()
        if not is_correct:
            print("'{}' is wrong answer ;(. Correct answer was '{}'. "
                  "\n Let's try again, {}!".format(ansver, result, name))
            break
        print("Correct!")
        i += 1
    else:
        print("Congratulations, {}!".format(name))
