from phrasehunter.game import Game
from phrasehunter.phrase import Phrase
def print_phrase(phrase_object: Phrase) -> None:
    print(f"The phrase is: {phrase_object.phrase}")


if __name__ == '__main__':
    while True:
        game: Game = Game()
        game.start()
        new_game: chr = input('Start a new game? y/n: ').lower()
        while new_game not in 'yn' or len(new_game) > 1:
            new_game: chr = input('Start a new game? y/n: ').lower()
        if new_game == 'y':
            continue
        else:
            exit()
