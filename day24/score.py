from turtle import Turtle

class ScoreBoard:
    def __init__(self, screen_height):
        self.turtle = Turtle()
        self.turtle.speed("fastest")
        self.turtle.penup()
        self.turtle.goto(0, screen_height / 2 - 30)
        self.turtle.color("white")

        with open("score.txt") as file:
            self.high_score = int(file.read())

        self.score = 0
        self.print_score()
        self.turtle.hideturtle()

    def print_score(self):
        self.turtle.clear()
        self.turtle.write(f"Score = {self.score}  Highest score = {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("score.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.print_score()

    def add_score(self):
        self.score += 1
        self.print_score()

    def game_over(self):
        self.turtle.goto(0, 0)
        self.turtle.write("GAME OVER", align="center", font=("Arial", 20, "normal"))