from dice import Dice

def test_dice_initialization():
    d = Dice()
    assert d.get_values() == [1, 1, 1, 1, 1]

def test_roll_all_dice():
    d = Dice()
    d.roll()
    vals = d.get_values()
    assert len(vals) == 5
    assert all(1 <= v <= 6 for v in vals)

def test_roll_selected_dice():
    d = Dice()
    d.values = [1, 1, 1, 1, 1]
    d.roll([0, 2, 4])
    vals = d.get_values()
    # Only indices 0, 2, 4 should possibly change
    assert vals[1] == 1 and vals[3] == 1
    assert all(1 <= v <= 6 for v in vals) 