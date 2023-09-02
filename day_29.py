#==== Imports ====#
from tkinter import *
import json
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip


#==== Function Definitions ====#
# Save Password
def save():
    site = website.get()
    mail = email.get()
    pass_ = password.get()
    credentials = {
        site: {
            "email": mail,
            "password": pass_
        }
    }

    if len(site) == 0 or len(pass_) == 0:
        messagebox.showwarning(title = "Empty Fields",
                               message = "Please don't leave any field empty")
    else:
        try:
            with open(FILE, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            with open(FILE, "w") as file:
                json.dump(credentials, file, indent = 4)
        else:
            data.update(credentials)

            with open(FILE, "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website.delete(0, END)
            password.delete(0, END)

# Password Generator
def gen_passcode():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    passcode = "".join(password_list)
    password.insert(0, passcode)
    pyperclip.copy(passcode)

# Find Password
def find_password():
    try:
        with open(FILE, "r") as file:
            data = json.load(file)

            site = website.get()
            mail = data[site]["email"]
            pass_ = data[site]["password"]
    except FileNotFoundError:
        messagebox.showwarning(title = "Missing File",
                               message = "No password file found")
    except KeyError:
        messagebox.showwarning(title = "Missing Data",
                               message = f"No details for {site} exists")
    else:
        messagebox.showinfo(title = site, message = f"Email/Username: {mail}\nPassword: {pass_}")



#==== Declarations ====#
window = Tk()
canvas = Canvas(width = 200, height = 200, highlightthickness = 0)
image = PhotoImage(file = "modules/password_logo.png")
website_label = Label(text = "Website:")
website = Entry(width = 21)
email_label = Label(text =  "Email/Username:")
email = Entry(width = 39)
password_label = Label(text = "Password:")
password = Entry(width = 21)
generate_password = Button(text = "Generate Password", command = gen_passcode)
add_password = Button(text = "Add", width = 36, command = save)
search = Button(text = "Search", width = 14, command = find_password)

sys_name = "USER"
FILE = f"C:/Users/{sys_name}/Desktop/saved_passwords.json"
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
        "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w",
        "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I",
        "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
        "V", "X", "Y", "Z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]


#==== Body ====#
# UI Setup
window.title("Savadow's Password Manager")
window.config(padx = 50, pady = 50)

canvas.create_image(100, 100, image = image)
canvas.grid(column = 1, row = 0)

website_label.grid(column = 0, row = 1)
website.grid(column = 1, row = 1)
website.focus()
email_label.grid(column = 0, row = 2)
email.grid(column = 1, row = 2, columnspan = 2)
email.insert(0, "ujuchimaraoke@gmail.com")
password_label.grid(column = 0, row = 3)
password.grid(column = 1, row = 3)
generate_password.grid(column = 2, row = 3)
add_password.grid(column = 1, row = 4, columnspan = 2)
search.grid(column = 2, row = 1)

window.mainloop()