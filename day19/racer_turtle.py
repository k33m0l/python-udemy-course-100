from turtle import Turtle
import random

class RacingTurtle:

    def __init__(self, color, order):
        self.color = color
        self.racer = Turtle()
        self.racer.color(color)
        self.racer.shape("turtle")
        self.racer.penup()

        self.racer.goto(x=-220, y=75 - 30 * order)

    def random_forward(self):
        self.racer.forward(random.randint(1, 10))