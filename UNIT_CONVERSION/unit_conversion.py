# UNIT_CONVERSION - Anzle Chavez
# prompts a user to enter a centimeter measurement and converts it in inches,
# feet , meters and kilometers. Your application should include **four separate
# functions** for each conversion. (12 marks)
import unittest


# Implement a test for each function
class TestStringMethods(unittest.TestCase):
    def test_conversions(self):
        self.assertEqual(conv_inches(2.54), 1)
        self.assertEqual(round(conv_feet(64), 2), 2.1)
        self.assertEqual(conv_metres(6400), 64)
        self.assertEqual(conv_km(250000), 2.5)


def conv_inches(cm: float) -> float:
    """
    Parameters
    ----------
    cm : float
       Length in centimetres
    Returns
    -------
    float
        returns conversion cm -> inch
    """
    return cm / 2.54


def conv_feet(cm: float) -> float:
    """
    Parameters
    ----------
    cm : float
        Length in centimetres
    Returns
    -------
    float
        returns conversion cm -> feet
    """
    return cm / 30.48


def conv_metres(cm: float) -> float:
    """
    Parameters
    ----------
    cm : float
        Length in centimetres
    Returns
    -------
    float
        returns conversion cm -> m
    """
    return cm / 100


def conv_km(cm: float) -> float:
    """
    Parameters
    ----------
    cm : float
        Length in centimetres
    Returns
    -------
    float
        returns conversion cm -> km
    """
    return cm / 100000


if __name__ == '__main__':
    USER_AMOUNT = int(input("How many cm will you convert?"))
    print(f"Converting {USER_AMOUNT} cm.\n")

    while True:
        # Prompt user for mode
        print(f"List of modes: I: INCHES, F: FEET, M: METRES, K: KILOMETRES")

        USER_MODE = input("What would you like the conversion to be?\n")

        try:
            # Match the letter given to the proper mode
            match USER_MODE:
                case "I":
                    print(conv_inches(USER_AMOUNT))
                    break
                case "F":
                    print(conv_feet(USER_AMOUNT))
                    break
                case "M":
                    print(conv_metres(USER_AMOUNT))
                    break
                case "K":
                    print(conv_km(USER_AMOUNT))
                    break
            raise ValueError
        # If the value is not one of the modes, the program will ask
        # for the value again. If this is not desired, the "continue"
        # can be replaced by "break".
        except ValueError:
            print("INCORRECT VALUE RECEIVED")
            continue
    unittest.main()
