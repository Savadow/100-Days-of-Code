from tkinter import *
from modules.day_34.quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_setup: QuizBrain):
        self.quiz = quiz_setup

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)

        self.score = Label(text = "Score: 0", bg = THEME_COLOR,
                           fg = "white")
        self.score.grid(row = 0, column = 1)

        self.canvas = Canvas(width = 300, height = 250, bg = "white")
        self.question = self.canvas.create_text(150, 125,
                                                width = 280,
                                                text = "QUESTION",
                                                fill = THEME_COLOR,
                                                font = ("Arial", 20, "italic"))
        self.canvas.grid(row = 1, column = 0, columnspan = 2, pady = 50)

        true = PhotoImage(file = "modules/day_34/images/true.png")
        false = PhotoImage(file="modules/day_34/images/false.png")
        self.true_button = Button(image = true, highlightthickness = 0,
                                  command = self.check_true)
        self.false_button = Button(image = false, highlightthickness = 0,
                                   command = self.check_false)
        self.true_button.grid(row = 2, column = 1)
        self.false_button.grid(row = 2, column = 0)

        self.get_next_question()


        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text = q_text)
        else:
            self.canvas.itemconfig(self.question,
                                   text = "You've reached the end of the quiz")
            self.true_button.config(state = "disabled")
            self.false_button.config(state="disabled")


    def check_true(self):
        check = self.quiz.check_answer("True")
        self.feedback(check)


    def check_false(self):
        check = self.quiz.check_answer("False")
        self.feedback(check)


    def feedback(self, check):
        if check:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")

        self.window.after(1000, self.get_next_question)