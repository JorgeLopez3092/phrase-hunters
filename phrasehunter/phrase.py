class Phrase:

    def __init__(self, phrase):
        self.phrase = phrase.lower()

    def display(self, guesses):
        for letter in self.phrase:
            if letter in guesses:
                print(f"{letter}", end=" ")
            else:
                print('_', end=" ")

    # def check_letter(self, letter):
    #     if letter in self.phrase:
    #          for char in self.phrase:
    #              if char == letter:
    #                  letter['guessed'] = True

    # def check_complete(self):
    #     for letter in self.phrase:
    #         if letter['guessed'] == False:
    #             return False

    #     return True
