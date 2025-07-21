from utils import is_valid_category, is_valid_dice_indices
from scorecard import ALL_CATEGORIES

def test_is_valid_category():
    assert is_valid_category(ALL_CATEGORIES[0])
    assert not is_valid_category("NotACategory")

def test_is_valid_dice_indices():
    assert is_valid_dice_indices([0, 1, 2, 3, 4])
    assert not is_valid_dice_indices([-1, 2, 3])
    assert not is_valid_dice_indices([0, 5]) 