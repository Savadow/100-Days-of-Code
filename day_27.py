##########
#### 1 ####
##########
# def add(*args):
#     total = 0
#     for num in args:
#         total += num
#
#     return total
#
# print(add(1, 2, 3, 4))

##########
#### 2 ####
##########
# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     return n
#
#
# print(calculate(2, add=3, multiply=5))

##########
#### 3 ####
##########
# class Car:
#     def __init__(self, **kwargs):
#         self.make = kwargs.get("make")  # Returns None if key not found
#         self.model = kwargs.get("model")
#
# car = Car(make = "Nissan", model = "GT-R")
# print(car.make)

##########
#### 4 ####
##########
# from tkinter import *

# def button_click():
#     print("Click Me")
#     label["text"] = input.get()
#
# # Window config
# window = Tk()
# window.title("GUI Way!!")
# window.minsize(width = 500, height = 300)
# # window.config(padx = 20, pady = 20)
#
# # Label Config
# label = Label(text = "Label 1", font = ("Arial", 24, "bold"))
# label.config(text = "Label")
# # label.pack()  # Allows the label to show
# # label.place(x = 0, y = 0)  # Allows for precise positioning
# label.grid(column = 0, row = 0)
# label.config(padx = 50, pady = 50)
#
# # Button Config
# button = Button(text = "Click Me", command = button_click)
# # button.pack()
# button.grid(column = 1, row = 1)
#
# button1 = Button(text = "Click")
# # button.pack()
# button1.grid(column = 2, row = 0)
#
# # Entry Config
# input = Entry(width = 30)
# # input.insert(END, string = "I'm an Entry!")  # Adds start text
# print(input.get())
# # input.pack()
# input.grid(column = 3, row = 2)
#
# # Text Config
# text = Text(height = 5, width = 30)
# text.focus()  # Puts cursor in textbox
# text.insert(END, "I'm a Text")
# print(text.get("1.0", END))
# text.pack()
#
# # Spinbox Config
# def spinbox_widget():
#     print(spinbox.get())
#
# spinbox = Spinbox(from_ = 0, to = 10, width = 5, command = spinbox_widget)
# spinbox.pack()
#
# # Scale Config
# def scale_widget(value):
#     print(value)
#
# scale = Scale(from_ = 0, to = 100, command = scale_widget)
# scale.pack()
#
# # Checkbox Config
# def checkbox_widget():
#     print(check.get())  # Prints 1 if On else 0
#
# check = IntVar()
# checkbutton = Checkbutton(text = "Is On?", variable = check, command = checkbox_widget)
# check.get()
# checkbutton.pack()
#
# # Radio Button Config
# def radio_widget():
#     print(radio.get())
#
# radio = IntVar()
# radio1 = Radiobutton(text = "Option 1", value = 1, variable = radio, command = radio_widget)
# radio2 = Radiobutton(text = "Option 2", value = 2, variable = radio, command = radio_widget)
# radio1.pack()
# radio2.pack()
#
# # List box config
# def listbox_widget(event):
#     print(listbox.get(listbox.curselection()))  # Gets current selection from listbox
#
# listbox = Listbox(height = 4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for fruit in fruits:
#     listbox.insert(fruits.index(fruit), fruit)
#
# listbox.bind("<<ListboxSelect>>", listbox_widget)
# listbox.pack()

# window.mainloop()

############
#### Main ####
############
#==== Imports ====#
from tkinter import *

#==== Function Definitions ====#
def convert():
    mile = float(entry.get())
    km = mile * 1.609
    value["text"] = km

#==== Declarations ====#
window = Tk()
entry = Entry(font = ("bold"), width = 7)
equal = Label(text = "is equal to", font = ("bold"))
miles = Label(text = "Miles", font = ("bold"))
value = Label(text = "0", font = ("bold"))
kilo = Label(text = "Km", font = ("bold"))
calculate = Button(text = "Calculate", font = ("bold"), command = convert)

#==== Body ====#
window.title("Miles to Km Converter")
# window.minsize(width = 370, height = 180)
window.config(padx = 20, pady = 20)

entry.grid(column = 1, row = 0)
equal.grid(column = 0, row = 1)
miles.grid(column = 2, row = 0)
value.grid(column = 1, row = 1)
kilo.grid(column = 2, row = 1)
calculate.grid(column = 1, row = 2)

window.mainloop()