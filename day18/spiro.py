from turtle import Turtle, Screen
import random

drawer = Turtle()
drawer.speed(0)

screen = Screen()
screen.colormode(255)

radius = 5
number_of_circles = int(360 / radius)
for _ in range(number_of_circles):
    red = random.randint(1, 255)
    blue = random.randint(1, 255)
    green = random.randint(1, 255)
    drawer.pencolor(red, blue, green)
    drawer.circle(100)
    drawer.left(radius)

screen.exitonclick()