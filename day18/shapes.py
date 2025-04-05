from turtle import Turtle, Screen
import random

drawer = Turtle()

screen = Screen()
screen.colormode(255)

def poligon(drawer, edge_num):
    angle = 360 / edge_num
    for _ in range(edge_num):
        drawer.forward(100)
        drawer.right(angle)

for edge_num in range(3, 12):
    red = random.randint(1, 255)
    blue = random.randint(1, 255)
    green = random.randint(1, 255)
    drawer.pencolor(red, blue, green)
    poligon(drawer, edge_num)

screen.exitonclick()