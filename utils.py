# utils.py
from scorecard import ALL_CATEGORIES

def is_valid_category(category):
    return category in ALL_CATEGORIES

def is_valid_dice_indices(indices, num_dice=5):
    return all(0 <= i < num_dice for i in indices) 