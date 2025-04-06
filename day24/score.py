from turtle import Turtle

class ScoreBoard:
    def __init__(self, screen_height):
        self.turtle = Turtle()
        self.turtle.speed("fastest")
        self.turtle.penup()
        self.turtle.goto(0, screen_height / 2 - 30)
        self.turtle.color("white")

        self.score = 0
        self.print_score()
        self.turtle.hideturtle()

    def print_score(self):
        self.turtle.clear()
        self.turtle.write(f"Score = {self.score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.turtle.goto(0, 0)
        self.turtle.write(f"GAME OVER!", align="center", font=("Arial", 20, "normal"))

    def add_score(self):
        self.score += 1
        self.print_score()