# yahtzee.py
from scorecard import Scorecard, ALL_CATEGORIES
from dice import Dice
from cli import display_dice, prompt_dice_to_reroll, display_scorecard, prompt_category_choice
from utils import is_valid_category, is_valid_dice_indices

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
                    category = prompt_category_choice(available_categories)
                    if not is_valid_category(category):
                        print("Invalid category. Try again.")
                        continue
                    if player.scorecard.is_category_used(category):
                        print("Category already used. Choose another.")
                        continue
                    # Calculate score (stub for now)
                    score = calculate_score_stub(category, dice.get_values())
                    player.scorecard.set_score(category, score)
                    print(f"Scored {score} points in {category}.")
                    break
        # End of game
        for player in self.players:
            print(f"\nFinal scorecard for {player.name}:")
            display_scorecard(player.scorecard)
            print(f"Total score: {player.scorecard.total_score()}")

def calculate_score_stub(category, dice_values):
    # TODO: Implement real scoring logic for each category
    # For now, just return the sum of dice as a placeholder
    return sum(dice_values)

def main():
    print("Welcome to Yahtzee!")
    name = input("Enter your name: ")
    player = Player(name)
    game = Game([player])
    game.play()

if __name__ == "__main__":
    main() 