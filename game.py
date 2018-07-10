import string
import random
import requests

class Game():

    def __init__(self):
        self.grid = self.random_grid()

    def random_grid(self):
        return [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, word):
        if not word:
            return False
        else:
            res = requests.get("https://wagon-dictionary.herokuapp.com/" + word)
            if not res.json()['found']:
                return False

        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return True

