# scorecard.py

ALL_CATEGORIES = [
    "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
    "Three of a Kind", "Four of a Kind", "Full House",
    "Four of a Kind", "Small Straight", "Large Straight",
    "Yahtzee", "Chance"
]

class Scorecard:
    def __init__(self):
        self.scores = {category: None for category in ALL_CATEGORIES}

    def is_category_used(self, category):
        return self.scores[category] is not None

    def set_score(self, category, score):
        self.scores[category] = score

    def total_score(self):
        return sum(score for score in self.scores.values() if score is not None) 