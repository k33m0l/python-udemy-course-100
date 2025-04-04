from question_model import Question

class QuizBrain:

    def __init__(self, questions):
        self.question_number = 0
        self.questions = questions

    def next_question(self):
        question = self.questions[self.question_number]
        answer = input(f"Q.{self.question_number + 1}: {question.text} (True/Flase): ").lower()
        if answer != "true" and answer != "false":
            print("Please provide a valid answer to the question.")
            return self.next_question()
        
        self.question_number += 1
        return self.validate_answer(question, answer)

    def validate_answer(self, question, answer):
        return question.answer.lower() == answer