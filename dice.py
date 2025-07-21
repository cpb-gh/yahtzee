# dice.py
import random

class Dice:
    def __init__(self, num_dice=5):
        self.num_dice = num_dice
        self.values = [1] * num_dice

    def roll(self, indices=None):
        if indices is None:
            self.values = [random.randint(1, 6) for _ in range(self.num_dice)]
        else:
            for i in indices:
                self.values[i] = random.randint(1, 6)

    def get_values(self):
        return self.values.copy() 