from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

brain = QuizBrain(question_bank)
for n in range(0, len(question_bank)):
    if not brain.next_question():
        print(f"Unfortunately you failed with the score of {n}")
        break
    else:
        if n == len(question_bank) - 1:
            print(f"You answered all the questions correctly! You finished the game with {n + 1} points")
        else:
            print("Correct, onto the next question.")