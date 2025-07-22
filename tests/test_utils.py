from utils import is_valid_category, is_valid_dice_indices
from scorecard import ALL_CATEGORIES
from yahtzee import match_category_input

def test_is_valid_category():
    assert is_valid_category(ALL_CATEGORIES[0])
    assert not is_valid_category("NotACategory")

def test_is_valid_dice_indices():
    assert is_valid_dice_indices([0, 1, 2, 3, 4])
    assert not is_valid_dice_indices([-1, 2, 3])
    assert not is_valid_dice_indices([0, 5])

def test_match_category_input_case_insensitive():
    cats = ["Ones", "Twos", "Threes"]
    assert match_category_input("ones", cats) == "Ones"
    assert match_category_input("ONES", cats) == "Ones"
    assert match_category_input("tWoS", cats) == "Twos"
    assert match_category_input("threes", cats) == "Threes"
    assert match_category_input("fours", cats) is None

def test_match_category_input_whitespace():
    cats = ["Full House", "Chance"]
    assert match_category_input("  full house  ", cats) == "Full House"
    assert match_category_input("chance", cats) == "Chance"
    assert match_category_input("  ", cats) is None 