#==== Imports ====#
from modules.day_15 import MENU, resources

#==== Variable Declaration ====#
brands = list(MENU.keys())
penny = 0.01
nickel = 0.05
dime = 0.1
quarter = 0.25

#==== Function Definition ====#
def check_resources(beverage, recipe, capacity):
    """
    Calculates the resources available
    :param beverage: Drink we want
    :param recipe: A dict that holds the quantity of ingredients needed to make beverage
    :param capacity: A dict that holds the quantity of ingredients in the machine
    :return: Statement telling you the status of your beverage
    """
    for k, v in recipe[beverage]["ingredients"].items():
        if v <= capacity[k]:

            print("Insert coins: ")
            pennies = int(input("How many pennies: "))
            nickels = int(input("How many nickels: "))
            dimes = int(input("How many dimes: "))
            quarters = int(input("How many quarters: "))

            money = (pennies * penny) + (nickels * nickel) + (dimes * dime) + (quarters * quarter)
            if money < recipe[beverage]["cost"]:
                return "Sorry not enough money. Money refunded"
        #
            else:
                resources["money"] += recipe[beverage]["cost"]
                for k, v in recipe[beverage]["ingredients"].items():
                    print(k, v)
                    capacity[k] -= v
                print(f"Your change is ${round(money - recipe[beverage]['cost'], 2)}")
                return f"Here's your {beverage}☕. Enjoy!"

        else:
            return f"Sorry there is not enough {k}"

#==== Body ====#
# A way to check if the machine is on/off
switch = True
while switch:
    beverage = input("What would you like? (espresso/latte/cappuccino):  ")

    # check to see if maintainer wants to turn off the machine
    if beverage == "off":
        switch = False

    # check for report
    elif beverage == "report":
        for k, v in resources.items():
            v = str(v)
            if k == "water" or k == "milk":
                v += "ml"
            elif k == "coffee":
                v += "g"
            else:
                v = "$" + v
            print(f"{k}: {v}")

    # check to see if there are available resource
    elif beverage in brands:
        print(check_resources(beverage, MENU, resources))

    else:
        print("Sorry, command not found!!")