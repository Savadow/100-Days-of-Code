##########
#### 1 ####
##########
# import requests
#
# response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
# iss_position = (latitude, longitude)
#
# print(iss_position)

##########
#### 2 ####
##########
# from tkinter import *
# import requests
#
# def get_quote():
#     response = requests.get(url = "https://api.kanye.rest")
#     response.raise_for_status()
#     data = response.json()
#     quote = data["quote"]
#     canvas.itemconfig(quote_text, text = quote, font=("Arial", 20, "bold"))
#
#
# window = Tk()
# window.title("Kanye Says...")
# window.config(padx=50, pady=50)
#
# canvas = Canvas(width=300, height=414)
# background_img = PhotoImage(file="modules/day_33/background.png")
# canvas.create_image(150, 207, image=background_img)
# quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes HERE", width=250,
#                                 font=("Arial", 30, "bold"), fill="white")
# canvas.grid(row=0, column=0)
#
# kanye_img = PhotoImage(file="modules/day_33/kanye.png")
# kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
# kanye_button.grid(row=1, column=0)
#
# window.mainloop()

##########
#### 3 ####
##########
import requests
from datetime import datetime as dt

MY_LAT = 4.815554
MY_LONG = 7.049844
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}
#
# response = requests.get(url = "https://api.sunrise-sunset.org/json",
#                         params = parameters)
# response.raise_for_status()
#
# data = response.json()
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
# print(sunrise)
# print(sunset)
#
# now = dt.now()
# print(now.hour)

#############
#### Main ####
#############
import smtplib
import time

EMAIL = "savadowdummy@gmail.com"
PASSWORD = "djzihcnhpmkhwjko"

def test_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT +5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True


def test_nighttime():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now = dt.now().hour

    if now <= sunrise or now >= sunset:
        return True


while True:
    time.sleep(60)
    if test_position() and test_nighttime():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = EMAIL, password = PASSWORD)
            connection.sendmail(from_addr = EMAIL,
                                to_addrs = "ujuchimaraoke@gmail.com",
                                msg = "Subject:Look Up👆🏻\n\nThe ISS is above you.")