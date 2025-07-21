from scorecard import Scorecard, ALL_CATEGORIES

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