################
#### Part 1 ####
################

# def is_leap(year):    
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0: 
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# def days_in_month(year, month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#     if is_leap(year) and month == 2:
#         return 29
    
#     return month_days[month - 1]


# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

##############
#### Main ####
##############

from modules.clear import clear

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number: "))

    for operation in operations:
        print(operation)

    chain = True
    while chain:
        symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number: "))

        arithmetic = operations[symbol]
        answer = arithmetic(num1, num2)
        print(f"{num1} {symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower()
        if choice == "n":
            chain = False
            clear()
            calculator()
        else:
            num1 = answer

calculator()