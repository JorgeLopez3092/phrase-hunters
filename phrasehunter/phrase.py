class Phrase:

    def __init__(self, phrase):
        self.phrase: str = phrase.lower()

    def display(self, guesses) -> None:
        for letter in self.phrase:
            if letter in guesses:
                print(f"{letter}", end=" ")
            else:
                print('_', end=" ")

    def check_guess(self, guess) -> bool:
        if guess in self.phrase:
            return True
        else:
            return False

    def check_complete(self, guesses) -> bool:
        phrase_set = set(self.phrase)
        guesses_set = set(guesses)
        return phrase_set.issubset(guesses_set)
    #     return True
