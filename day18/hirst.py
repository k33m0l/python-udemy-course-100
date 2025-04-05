from turtle import Turtle, Screen
from colors import color_list, get_random

drawer = Turtle()
drawer.speed(0)
drawer.penup()

#set init pos
drawer.right(90)
drawer.forward(200)
drawer.left(90)

screen = Screen()
screen.colormode(255)

for count in range(100):
    drawer.dot(20, get_random())
    drawer.forward(50)

    if (count + 1) % 10 == 0:
        drawer.left(90)
        drawer.forward(50)
        drawer.left(90)
        drawer.forward(50 * 10)
        drawer.left(180)

screen.exitonclick()