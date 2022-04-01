"""Summary
A fast food restaurant charges $7 for burgers, $3 for fries,
and $2 for drinks.

a) Create an Order application that prompts the employee for the number of
burgers, fries, and sodas and then displays the total, the tax (13%),
and the final cost.

b) Modify Order to prompt the employee for the amount tendered and then
display the change due.
"""

# STEPS REQUIRED:
# 1. Prompt employee for 3 variables.
#   1. Burgers
#   2. Fries 
#   3. Sodas

# 2. def Total(burgers, fries, sodas):
#   calculates the total based off of prices and the tax.
#   TODO: put the prices in a dict, so that it is extensible.
#   returns a list with the first element as the total, and the second tax.

# 3. prints the total to the console

# 4. Asks for 1 variable: amount tendered.

# 5. def Change(total, amount_tendered):
#   return total - amount tendered'


def total(b, f, d) -> (float, float):
    """Calculates the total of money due from the burgers, fries, and drinks.
    Args:
        b (int): amount of burgers
        f (int): amount of fries
        d (int): amount of drinks
    Returns:
        float, float: returns the no_tax value, then [2] being the tax
    """
    no_tax = float((b * 7 + f * 3 + d * 2))
    tax = no_tax * 0.13

    return (no_tax, tax)


if __name__ == "__main__": 
    burgers = float(input("How many burgers have you ordered? "))
    fries = float(input("How many fries have you ordered? "))
    drinks = float(input("How many sodas have you ordered? "))

    # Calculate the user total() and adds return values for the amount w/ tax.
    user_total = total(burgers, fries, drinks)
    total_taxed = user_total[0] + user_total[1]

    # Initial values printed to user: without tax and with tax.
    print(
        f"Your total comes to {user_total[0]}, and with tax, {total_taxed}.\n"
    )

    # Create a loop to run until the cash is properly handled, and change is displayed
    while True:
        tendered = input("How much cash will you be paying? ")

        # The amount given must be more than the amount needed with tax.
        if tendered > total_taxed:
            amount_tendered = tendered - user_total[1]
        else:  # handle exception if amount is too low
            print("Incorrect value; this amount is too low.\n")
            continue

        print(f"Your final change is {amount_tendered}\nThank you for ordering!")
        break
