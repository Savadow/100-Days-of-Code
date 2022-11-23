##########
#### 1 ####
##########
# import smtplib
#
# email = "savadowdummy@gmail.com"
# password = "djzihcnhpmkhwjko"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user = email, password = password)
#     connection.sendmail(from_addr = email, to_addrs = "ujuchimaraoke@gmail.com",
#                         msg = "Subject:Hello\n\nHi, wagwan")

##########
#### 2 ####
##########
# import datetime as dt
#
# now = dt.datetime.now()
# yr = now.year
#
# dob = dt.datetime(year = 2002, month = 6, day = 20)
# print(dob)

##########
#### 3 ####
##########
# import datetime as dt
# import random
# import smtplib
#
# if dt.datetime.now().weekday() == 5:
#     with open("modules/day_32/quotes.txt") as quote_file:
#         quotes = quote_file.readlines()
#         quote = random.choice(quotes).strip("\n")
#
#     email = "savadowdummy@gmail.com"
#     password = "djzihcnhpmkhwjko"
#
#     with smtplib.SMTP("smtp.gmail.com") as connection:
#         connection.starttls()
#         connection.login(user=email, password=password)
#         connection.sendmail(from_addr = email, to_addrs = "ujuchimaraoke@gmail.com",
#                             msg = f"Subject:Have a nice week\n\n{quote}")

############
#### Main ####
############
#==== Imports ====#
import pandas
import datetime as dt
import os
import random
import smtplib

#==== Declarations ====#
data = pandas.read_csv("modules/day_32/birthdays.csv")
dob = data.to_dict(orient = "records")

today = (dt.datetime.now().month, dt.datetime.now().day)

path = "modules/day_32/letter_templates"
dirs = os.listdir(path)
letter = random.choice(dirs)

EMAIL = "savadowdummy@gmail.com"
PASSWORD = "djzihcnhpmkhwjko"

#==== Body ====#
for birthday in dob:
    birthdate = (birthday["month"], birthday["day"])

    if today == birthdate:
        with open(f"{path}/{letter}") as file:
            content = file.read()

        message = content.replace("[NAME]", birthday["name"])
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = EMAIL, password = PASSWORD)
            connection.sendmail(from_addr = EMAIL, to_addrs = birthday["email"],
                                msg = f"Subject:Happy Birthday\n\n{message}n")