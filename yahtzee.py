# yahtzee.py
from scorecard import Scorecard

class Player:
    def __init__(self, name):
        self.name = name
        self.scorecard = Scorecard()

class Game:
    def __init__(self, players):
        self.players = players
        self.round = 1 