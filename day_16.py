#############
#### Part ! ####
#############

# from turtle import Turtle, Screen
#
# tim = Turtle()
# print(tim)
# tim.shape("turtle")
# tim.color("blue")
# tim.forward(100)
#
# led = Screen()
# print(led.canvheight)
# led.exitonclick()

############
#### Main ####
############

#==== Imports ====#
from modules.menu import Menu, MenuItem
from modules.coffee_maker import CoffeeMaker
from modules.money_machine import MoneyMachine

#==== Variable Declaration ====#
# Creating class objects
item = Menu()
order = CoffeeMaker()
money = MoneyMachine()

# Creating normal variables
drinks = item.get_items()

#==== Body ====#
# A way to keep the machine on or to turn it off
switch = True
while switch:
    beverage = input(f"What would you like? ({drinks}): ")

    # check to see if maintainer wants to turn off the machine
    if beverage == "off":
        switch = False

    # check for report
    if beverage == "report":
        order.report()
        money.report()

    else:
        option = item.find_drink(beverage)
        if order.is_resource_sufficient(option):
            if money.make_payment(option.cost):
                order.make_coffee(option)