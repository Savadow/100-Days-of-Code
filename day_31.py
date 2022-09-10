#==== Imports ====#
from tkinter import *
import pandas
import random


#==== Function Definitions ====#
def next_card():
    global card, flip_time

    window.after_cancel(flip_time)
    card = random.choice(learn)
    canvas.itemconfig(language, text = "French", fill = "black")
    canvas.itemconfig(question, text = card["French"], fill = "black")
    canvas.itemconfig(card_background, image=card_front)
    flip_time = window.after(3000, func = flip)

def flip():
    canvas.itemconfig(language, text = "English", fill ="white")
    canvas.itemconfig(question, text = card["English"], fill ="white")
    canvas.itemconfig(card_background, image = card_back)

def remove_card():
    learn.remove(card)
    df = pandas.DataFrame(learn)
    df.to_csv("modules/day_31/words/words_to_learn.csv", index = False)

    next_card()


#==== Declarations ====#
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
card_front = PhotoImage(file ="modules/day_31/elements/card_front.png")
card_back = PhotoImage(file ="modules/day_31/elements/card_back.png")
correct = PhotoImage(file ="modules/day_31/elements/right.png")
incorrect = PhotoImage(file ="modules/day_31/elements/wrong.png")

card = {}
learn = {}
try:
    df = pandas.read_csv("modules/day_31/words/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("modules/day_31/words/french_words.csv")
    learn = data.to_dict(orient = "records")
else:
    learn = df.to_dict(orient = "records")

canvas = Canvas(width = 800, height = 530, bg = BACKGROUND_COLOR,
                highlightthickness = 0)
right = Button(image = correct, bg = BACKGROUND_COLOR, highlightthickness = 0,
               command = remove_card)
wrong = Button(image = incorrect, bg = BACKGROUND_COLOR, highlightthickness = 0,
               command = next_card)


#==== Body ====#
window.title("Savadow's Flash Card")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)
flip_time = window.after(3000, func = flip)

card_background = canvas.create_image(400, 265, image = card_front)
language = canvas.create_text(400, 132, text = "Language", fill = "black",
                              font = ("Arial", 40, "italic"))
question = canvas.create_text(400, 265, text = "Word", fill = "black",
                              font = ("Arial", 60, "bold"))
canvas.grid(column = 0, row = 0, columnspan = 2)

right.grid(column = 1, row = 1)
wrong.grid(column = 0, row = 1)

next_card()

window.mainloop()