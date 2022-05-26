class QuizBrain:

    def __init__(self, question_list):
        self.number = 0
        self.questions = question_list
        self.score = 0

    def still_has_questions(self):
        if self.number < len(self.questions):
            return True
        else:
            return False

    def next_question(self):
        q_text = self.questions[self.number]
        self.number += 1
        user = input(f"Q.{self.number}: {q_text.text} (True or False)?: ").lower()
        self.check_answer(user, q_text.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong!!")
            print(f"The correct answer is {correct_answer}")

        print(f"Your score is {self.score}/{self.number}\n")