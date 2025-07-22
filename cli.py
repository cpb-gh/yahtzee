# cli.py

def display_dice(dice_values):
    print(f"Dice: {dice_values}")

def prompt_dice_to_reroll():
    return input("Enter dice indices to re-roll (e.g., 1 3 4), or press Enter to keep all: ")

def display_scorecard(scorecard):
    print("Scorecard:")
    for category, score in scorecard.scores.items():
        print(f"  {category}: {score if score is not None else '-'}")
    # Show upper section bonus
    if hasattr(scorecard, 'has_upper_bonus') and hasattr(scorecard, 'upper_section_total'):
        bonus = 35 if scorecard.has_upper_bonus() else 0
        print(f"  Upper Section Bonus: {bonus} ({'AWARDED' if bonus else 'not awarded'})")

def prompt_category_choice(available_categories):
    print(f"Available categories: {', '.join(available_categories)}")
    return input("Choose a category: ") 