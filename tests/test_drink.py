import test_driven_development_example.drink as drink


def test_drink_looks_over_25():
    assert drink.canBuyAlcohol(True) == True


def test_drink_rejected_if_no_id():
    assert drink.canBuyAlcohol(False) == False


def test_too_young_to_buy_alcohol():
    assert drink.canBuyAlcohol(False, 17) == False


def test_old_enough_to_buy_alcohol():
    assert drink.canBuyAlcohol(False, 19) == True