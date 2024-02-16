from phrasehunter.game import Game
from phrasehunter.phrase import Phrase

game: Game = Game()


def print_phrase(phrase_object: Phrase) -> None:
    print(f"The phrase is: {phrase_object.phrase}")


if __name__ == '__main__':
    # print(game.active_phrase.phrase)
    # game.active_phrase.display(game.guesses)
    game.start()
