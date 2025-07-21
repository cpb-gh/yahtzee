from scorecard import Scorecard, ALL_CATEGORIES
from yahtzee import calculate_score

def test_scorecard_initialization():
    sc = Scorecard()
    assert all(sc.scores[cat] is None for cat in ALL_CATEGORIES)

def test_is_category_used():
    sc = Scorecard()
    cat = ALL_CATEGORIES[0]
    assert not sc.is_category_used(cat)
    sc.set_score(cat, 5)
    assert sc.is_category_used(cat)

def test_set_and_get_score():
    sc = Scorecard()
    cat = ALL_CATEGORIES[1]
    sc.set_score(cat, 10)
    assert sc.scores[cat] == 10

def test_total_score():
    sc = Scorecard()
    sc.set_score(ALL_CATEGORIES[0], 3)
    sc.set_score(ALL_CATEGORIES[1], 6)
    sc.set_score(ALL_CATEGORIES[2], 9)
    assert sc.total_score() == 18

# --- Scoring logic tests ---

def test_ones():
    assert calculate_score("Ones", [1, 2, 1, 4, 1]) == 3

def test_twos():
    assert calculate_score("Twos", [2, 2, 3, 4, 5]) == 4

def test_threes():
    assert calculate_score("Threes", [3, 3, 3, 4, 5]) == 9

def test_fours():
    assert calculate_score("Fours", [4, 4, 4, 4, 1]) == 16

def test_fives():
    assert calculate_score("Fives", [5, 2, 5, 5, 1]) == 15

def test_sixes():
    assert calculate_score("Sixes", [6, 6, 6, 2, 1]) == 18

def test_three_of_a_kind():
    assert calculate_score("Three of a Kind", [2, 2, 2, 4, 5]) == 15
    assert calculate_score("Three of a Kind", [2, 2, 3, 4, 5]) == 0

def test_four_of_a_kind():
    assert calculate_score("Four of a Kind", [3, 3, 3, 3, 5]) == 17
    assert calculate_score("Four of a Kind", [3, 3, 3, 4, 5]) == 0

def test_full_house():
    assert calculate_score("Full House", [2, 2, 3, 3, 3]) == 25
    assert calculate_score("Full House", [2, 2, 2, 2, 3]) == 0

def test_small_straight():
    assert calculate_score("Small Straight", [1, 2, 3, 4, 6]) == 30
    assert calculate_score("Small Straight", [2, 3, 4, 5, 2]) == 30
    assert calculate_score("Small Straight", [1, 3, 4, 5, 6]) == 30
    assert calculate_score("Small Straight", [1, 1, 3, 4, 6]) == 0

def test_large_straight():
    assert calculate_score("Large Straight", [1, 2, 3, 4, 5]) == 40
    assert calculate_score("Large Straight", [2, 3, 4, 5, 6]) == 40
    assert calculate_score("Large Straight", [1, 2, 3, 4, 6]) == 0

def test_yahtzee():
    assert calculate_score("Yahtzee", [6, 6, 6, 6, 6]) == 50
    assert calculate_score("Yahtzee", [6, 6, 6, 6, 5]) == 0

def test_chance():
    assert calculate_score("Chance", [1, 2, 3, 4, 5]) == 15
    assert calculate_score("Chance", [6, 6, 6, 6, 6]) == 30 