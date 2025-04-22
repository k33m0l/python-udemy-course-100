from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quit App")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.scole_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.scole_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            text="The question will appear here, please wait",
            fill=THEME_COLOR,
            font=FONT,
            width=280
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, bg=THEME_COLOR, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, bg=THEME_COLOR, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.scole_label.config(text=f"Score: {self.quiz_brain.score}")
            question = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the test.")

    def true_pressed(self):
        is_right = self.quiz_brain.check_answer("true")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz_brain.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)