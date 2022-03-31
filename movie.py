import unittest
"""
Write an algorithm or pseudocode and  flowchart that tells the user what type
of movie they can attend based on their age, if they are with their parents, 
and their amount of money.

- Under 13: G
- Under 13 w/ parent: G, PG
- 13 and Over and Under 16 G, PG
- 13 and Over and Under 16 w/ parent G, PG, R
- 16 and Over G, PG, R
- Matinee: .50
- Evening: .50
"""


class TestStringMethods(unittest.TestCase):
    def test_age(self):
        self.assertListEqual(age_verifier(16, True), ["G", "PG", "R"])
        self.assertListEqual(age_verifier(13, True), ["G", "PG"])

    def test_money(self):
        self.assertListEqual(money_verifier(12.0), ["Matinee", "Evening"])
        self.assertListEqual(money_verifier(0.0), [False])


def age_verifier(age: int, parent: bool) -> list:
    """Verifies what types of movies the person can watch, based on their age
    and the presence of a parent\n
    Args:
        age (int): age of person
        parent (bool): whether the person has a parent or not
    Returns:\n
        list: returns list of available movies
    """
    if age > 16:
        return ["G", "PG", "R"]
    elif age >= 13:
        if parent:
            return ["G", "PG", "R"]
        else:
            return ["G", "PG"]
    else:
        if parent:
            return ["G", "PG"]
        else:
            return ["G"]


def money_verifier(cash: float) -> list:
    """Verifies what tickets the amount of cash could purchase.\n
    
    Args:
        cash (float): Cash given by customer\n
    
    Returns:
        str: Returns possible tickets from matinee and/or evening
    """
    if cash >= 10.50:
        return ["Matinee", "Evening"]
    elif cash >= 7.50:
        return ["Matinee"]
    else:
        return [False]


def prompt_customer() -> dict:
    U_CASH = float(input("How much cash will you bring? "))
    U_AGE = int(input("What is your age? "))
    U_PARENT = bool(input("Do you have a parent with you?"))

    result = {
        "cash": U_CASH,
        "age": U_AGE,
        "parent": U_PARENT
    }

    return result


# unittest.main()
if __name__ == "__main__":
    USER = prompt_customer()
    CASH = USER["cash"]
    AGE = USER["age"]
    PARENT = USER["parent"] 

    allowed_movies = age_verifier(AGE, PARENT)
    allowed_tickets = money_verifier(CASH)

    print(f"For a {AGE} year(s) old with {CASH}$\n{allowed_movies}, {allowed_tickets}")

    unittest.main()