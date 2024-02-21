from typing import List

from phrasehunter.phrase import Phrase
import random


class Game:
    def __init__(self):
        self.missed: int = 0
        self.phrases: List[Phrase] = self.create_phrases()
        self.active_phrase: Phrase = self.get_random_phrase()
        self.guesses: List[str] = [" "]

    @staticmethod
    def create_phrases() -> List[Phrase]:
        phrases_pool: List[str] = ['Just do it', 'Carpe diem', 'Game on', 'Easy as pie', 'True north', 'Hello world',
                                   'Hattori Hanzo steel', 'Wiggle your big toe', 'You and I have unfinished business',
                                   'May the force be with you']
        phrases = []
        while len(phrases) < 5:
            new_phrase = phrases_pool.pop(random.randrange(len(phrases_pool)))
            phrases.append(Phrase(new_phrase))
        # print(phrases)
        return phrases

    def get_random_phrase(self) -> Phrase:
        return self.phrases[random.randrange(len(self.phrases))]

    @staticmethod
    def get_guess() -> chr:
        guess: str = input("\nEnter a letter: ")
        while not guess or not guess[0].isalpha():
            guess: str = input("Must enter a letter: ")

        return guess[0]

    @staticmethod
    def welcome() -> None:
        print('''
        ******************************
           Welcome to Phrase Hunter
        ******************************''')

    @staticmethod
    def game_over(missed: int) -> None:
        if missed < 5:
            print('\nCongratulations!  You win!')
        else:
            print('\nBummer!  Try  again!')

    def start(self):
        self.welcome()
        while self.missed < 5 and not self.active_phrase.check_complete(self.guesses):
            print(f"\n\nNumber missed: {sum(1 for guess in self.guesses if guess not in self.active_phrase.phrase)}\n")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            print(user_guess)
            # self.check_guess(user_guess)
            self.guesses.append(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
            self.active_phrase.display(self.guesses)

        self.game_over(self.missed)
