
def canBuyAlcohol(looks_over_25, id_age=None):
    if looks_over_25:
        return True
    elif not id_age or id_age <= 17:
        return False
    elif id_age >= 18:
        return True
