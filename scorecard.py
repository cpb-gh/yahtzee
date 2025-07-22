# scorecard.py

ALL_CATEGORIES = [
    "Ones", "Twos", "Threes", "Fours", "Fives", "Sixes",
    "Three of a Kind", "Full House",
    "Four of a Kind", "Small Straight", "Large Straight",
    "Yahtzee", "Chance"
]

UPPER_CATEGORIES = ["Ones", "Twos", "Threes", "Fours", "Fives", "Sixes"]
UPPER_BONUS_THRESHOLD = 63
UPPER_BONUS_SCORE = 35

class Scorecard:
    def __init__(self):
        self.scores = {category: None for category in ALL_CATEGORIES}

    def is_category_used(self, category):
        return self.scores[category] is not None

    def set_score(self, category, score):
        self.scores[category] = score

    def upper_section_total(self):
        return sum(self.scores[cat] for cat in UPPER_CATEGORIES if self.scores[cat] is not None)

    def has_upper_bonus(self):
        return self.upper_section_total() >= UPPER_BONUS_THRESHOLD

    def total_score(self):
        total = sum(score for score in self.scores.values() if score is not None)
        if self.has_upper_bonus():
            total += UPPER_BONUS_SCORE
        return total 