from turtle import Turtle, Screen
import random

drawer = Turtle()
drawer.width(10)
drawer.speed(10)

screen = Screen()
screen.colormode(255)

directions = [0, 90, 180, 270]
def walk(drawer):
    drawer.right(random.choice(directions))
    drawer.forward(20)

for _ in range(200):
    red = random.randint(1, 255)
    blue = random.randint(1, 255)
    green = random.randint(1, 255)
    drawer.pencolor(red, blue, green)
    walk(drawer)

screen.exitonclick()