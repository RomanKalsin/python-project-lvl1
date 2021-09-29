#!/usr/bin/env python3


from brain_games.games.logic import game_logic
from brain_games.games.prime import tutorial, game


def main():
    game_logic(tutorial, game)


if __name__ == "__main__":
    main()
