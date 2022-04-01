"""
ALGORITHM_MOVIETYPE - Anzle Chavez
Write an algorithm or pseudocode and flowchart that tells the user what type
of movie they can attend based on their age, if they are with their parents,
and their amount of money.

- Under 13: G
- Under 13 w/ parent: G, PG
- 13 and Over and Under 16 G, PG
- 13 and Over and Under 16 w/ parent G, PG, R
- 16 and Over G, PG, R
- Matinee: 7.50
- Evening: 10.50
"""
import unittest

# My preferred method of verifying data such as the rating of the movie
# is with dictionaries and lists.

# In this program, I take in the age as an integer, whether
# the parent is present as a boolean, and how much cash they have as a float.
# From both functions, age_verifier, and money_verifier, it returns a list of
# the available options. This is very useful when making a program because
# instead of filtering through random strings, code can just check for the
# presence of an element such as an "R" movie, and from that result,
# take action.


class Tests(unittest.TestCase):
    def test_age(self):
        # Even if the parent is not present, if child is over 16,
        # they should have access to R-rated movies
        self.assertListEqual(age_verifier(16, False), ["G", "PG", "R"])
        # Children exactly 12 with a parent should be able to see PG movies
        # but NOT R-movies.
        self.assertListEqual(age_verifier(12, True), ["G", "PG"])

    def test_money(self):
        # If the person has exactly 10.49, they do not have enough to
        # see the Matinee and the evening show.
        self.assertListEqual(money_verifier(10.49), ["Matinee"])
        # Special case is when the money is 0, it must return False,
        # meaning that there is not enough money to purchase a ticket
        self.assertListEqual(money_verifier(0.0), [])


def age_verifier(age: int, parent: bool) -> list:
    """Verifies what types of movies the person can watch, based on their age
    and the presence of a parent\n
    Args:
        age (int): age of person
        parent (bool): whether the person has a parent or not
    Returns:
        list: returns list of available movies
    """
    if age >= 16:
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
        return []


def prompt_customer() -> dict:
    # Prompts the customer
    U_AGE = int(input("What is your age? "))
    # If the person is over 16, does not need any parent,
    # thus can skip to setting the cash amount.
    if U_AGE >= 16:
        # Sets U_PARENT as true, since it does not matter,
        # and I don't know how to make optional parameters.
        U_PARENT = True
    else:
        U_PARENT = bool(input("Do you have a parent with you?"))
    U_CASH = float(input("How much cash will you bring? "))

    result = {
        "cash": U_CASH,
        "age": U_AGE,
        "parent": U_PARENT
    }

    return result


if __name__ == "__main__":
    # make 4 constants:
    # USER: parent constant returning the others in the hashmap.
    # CASH: amount of cash as a float
    # AGE: age in int
    # PARENT: boolean whether the parent is present
    USER = prompt_customer()
    CASH = USER["cash"]
    AGE = USER["age"]
    PARENT = USER["parent"]

    # Create two constants and pass in the created variables.
    # ALLOWED_MOVIES: takes in the age and the parent bool
    # ALLOWED_TICKTES: verifies the cash given
    ALLOWED_MOVIES = age_verifier(AGE, PARENT)
    ALLOWED_TICKETS = money_verifier(CASH)

    # Print out age and cash, then the allowed movies and tickets
    print(f"For a {AGE} year old with {CASH}$ and parent = {PARENT}\n")

    # While I do see the value in using a for loop to iterate
    # through the array and displaying all the values like that,
    # the brackets around the strings are not all that ugly.
    print(f"{ALLOWED_MOVIES}, {ALLOWED_TICKETS}")

    # Runs the test declared up top.
    unittest.main()
