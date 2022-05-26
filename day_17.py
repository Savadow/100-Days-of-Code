#############
#### Part 1 ####
#############

# class User:
#
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#
# user_1 = User("001", "savadow")
# user_2 = User("002", "nedum")
#
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)
# print(user_2.followers)
# print(user_2.following)

############
#### Main ####
############

#==== Imports ====#
from modules.question_model import Question
from modules.data import question_data
from modules.quiz_brain import QuizBrain

#==== Variable Declaration ====#
question_bank = []
quiz = QuizBrain(question_bank)

#==== Body ====#
for i in range(len(question_data)):
    question = question_data[i]["text"]
    answer = question_data[i]["answer"]
    question_bank.append(Question(question, answer))

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your score was: {quiz.score}/{quiz.number}")