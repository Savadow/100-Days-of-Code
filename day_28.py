#==== Imports ====#
from tkinter import *

#==== Function Definitions ====#
# Countdown Mechanism
def countdown(count):
    global timer

    minute = count // 60
    second = count % 60
    if second < 10:
        second = f"0{second}"

    canvas.itemconfig(timer_text, text = f"{minute}:{second}")
    if count > 0:
        timer  = window.after(1000, countdown, count - 1)
    else:
        start_timer()

        marks = ""
        complete = reps // 2
        for _ in range(complete):
            marks += "✔"

        ticks["text"] = marks

# Timer Mechanism
def start_timer():
    global reps
    reps += 1

    work = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN *60

    if reps == 8:
        # window.
        countdown(long_break)
        timer_label.config(text ="Break", fg = RED)
    elif reps % 2 != 0:
        countdown(work)
        timer_label.config(text="Work", fg=GREEN)
    else:
        countdown(short_break)
        timer_label.config(text="Break", fg=PINK)

# Timer Reset
def reset_timer():
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    timer_label["text"] = "Timer"
    ticks["text"] = ""
    reps = 0

#==== Declarations ====#
# Constants
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"

WORK_MIN = 40
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 30

# Variables
window = Tk()
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
image = PhotoImage(file = "modules/tomato.png")
timer_label = Label(text ="Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 50))
start = Button(text = "Start", command = start_timer, highlightthickness = 0)
ticks = Label(fg = GREEN, bg = YELLOW)
reset = Button(text = "Reset", highlightthickness = 0, command = reset_timer)

timer = None
reps = 0

#==== Body ====#
# UI Setup
window.title("Savadow's Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

canvas.create_image(100, 112, image = image)
timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white",
                                font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)

timer_label.grid(column = 1, row = 0)
start.grid(column = 0, row = 2)
ticks.grid(column = 1, row = 3)
reset.grid(column = 2, row = 2)

window.mainloop()