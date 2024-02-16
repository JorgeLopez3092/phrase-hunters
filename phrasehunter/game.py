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

    def check_guess(self, guess: chr) -> bool:
        if guess in self.active_phrase:
            print("YAY")
            return True
        else:
            print("Bummer!")
            return False

    def start(self):
        self.welcome()
        print(f"\n\nNumber missed: {sum(1 for guess in self.guesses if guess not in self.active_phrase.phrase)}\n")
        self.active_phrase.display(self.guesses)
        user_guess = self.get_guess()
        print(user_guess)
        self.guesses.append(user_guess)
        self.active_phrase.display(self.guesses)
