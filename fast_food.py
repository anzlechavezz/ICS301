# A fast food restaurant charges $7 for burgers, $3 for fries,
# and $2 for drinks.

# a) Create an Order application that prompts the employee for the number of
# burgers, fries, and sodas and then displays the total, the tax (13%),
# and the final cost.

# b) Modify Order to prompt the employee for the amount tendered and then
# display the change due.

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
    no_tax = (b * 7 + f * 3 + d * 2)
    tax = no_tax * 0.13 + no_tax

    return (no_tax, tax)


if __name__ == "__main__": 
    burgers = float(input("How many burgers have you ordered? "))
    fries = float(input("How many fries have you ordered? "))
    drinks = float(input("How many sodas have you ordered? "))

    user_total = total(burgers, fries, drinks)

    print(
        f"Your total comes to {user_total[0]}, and with tax, {user_total[1]}.\n"
    )

    while True:
        tendered = input("How much cash will you be paying? ")

        if tendered > user_total[1]:
            amount_tendered = tendered - user_total[1]
        else:
            print("Incorrect value.\n")
            continue
        print(f"Your final total is {amount_tendered}")
        break

return 


