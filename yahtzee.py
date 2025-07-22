# yahtzee.py
from scorecard import Scorecard, ALL_CATEGORIES
from dice import Dice
from cli import display_dice, prompt_dice_to_reroll, display_scorecard, prompt_category_choice
from utils import is_valid_category, is_valid_dice_indices
from collections import Counter

class Player:
    def __init__(self, name):
        self.name = name
        self.scorecard = Scorecard()

class Game:
    def __init__(self, players):
        self.players = players
        self.round = 1

    def play(self):
        for round_num in range(1, 14):
            for player in self.players:
                print(f"\nRound {round_num} — Player: {player.name}")
                dice = Dice()
                rolls_left = 3
                dice.roll()
                while rolls_left > 1:
                    display_dice(dice.get_values())
                    reroll_input = prompt_dice_to_reroll()
                    if not reroll_input.strip():
                        break
                    try:
                        indices = [int(i) - 1 for i in reroll_input.strip().split()]
                        if not is_valid_dice_indices(indices, dice.num_dice):
                            print("Invalid dice indices. Try again.")
                            continue
                        dice.roll(indices)
                        rolls_left -= 1
                    except ValueError:
                        print("Invalid input. Please enter numbers separated by spaces.")
                # Final dice
                display_dice(dice.get_values())
                display_scorecard(player.scorecard)
                available_categories = [cat for cat in ALL_CATEGORIES if not player.scorecard.is_category_used(cat)]
                while True:
                    category_input = prompt_category_choice(available_categories)
                    category = match_category_input(category_input, available_categories)
                    if not category:
                        print("Invalid category. Try again.")
                        continue
                    if player.scorecard.is_category_used(category):
                        print("Category already used. Choose another.")
                        continue
                    # Calculate score (real logic)
                    score = calculate_score(category, dice.get_values())
                    player.scorecard.set_score(category, score)
                    print(f"Scored {score} points in {category}.")
                    break
        # End of game
        for player in self.players:
            print(f"\nFinal scorecard for {player.name}:")
            display_scorecard(player.scorecard)
            print(f"Total score: {player.scorecard.total_score()}")

def match_category_input(user_input, available_categories):
    """
    Return the matching category from available_categories (case-insensitive), or None if not found.
    """
    for cat in available_categories:
        if cat.lower() == user_input.strip().lower():
            return cat
    return None

def calculate_score(category, dice_values):
    counts = Counter(dice_values)
    unique = sorted(set(dice_values))
    if category == "Ones":
        return dice_values.count(1) * 1
    elif category == "Twos":
        return dice_values.count(2) * 2
    elif category == "Threes":
        return dice_values.count(3) * 3
    elif category == "Fours":
        return dice_values.count(4) * 4
    elif category == "Fives":
        return dice_values.count(5) * 5
    elif category == "Sixes":
        return dice_values.count(6) * 6
    elif category == "Three of a Kind":
        if any(v >= 3 for v in counts.values()):
            return sum(dice_values)
        return 0
    elif category == "Four of a Kind":
        if any(v >= 4 for v in counts.values()):
            return sum(dice_values)
        return 0
    elif category == "Full House":
        if sorted(counts.values()) == [2, 3]:
            return 25
        return 0
    elif category == "Small Straight":
        # 4 sequential dice: 1-2-3-4, 2-3-4-5, 3-4-5-6
        straights = [set([1,2,3,4]), set([2,3,4,5]), set([3,4,5,6])]
        for straight in straights:
            if straight.issubset(set(dice_values)):
                return 30
        return 0
    elif category == "Large Straight":
        # 5 sequential dice: 1-2-3-4-5, 2-3-4-5-6
        if set([1,2,3,4,5]) == set(dice_values) or set([2,3,4,5,6]) == set(dice_values):
            return 40
        return 0
    elif category == "Yahtzee":
        if len(counts) == 1:
            return 50
        return 0
    elif category == "Chance":
        return sum(dice_values)
    else:
        return 0

def main():
    print("Welcome to Yahtzee!")
    name = input("Enter your name: ")
    player = Player(name)
    game = Game([player])
    game.play()

if __name__ == "__main__":
    main() 