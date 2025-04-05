from turtle import Turtle, Screen

drawer = Turtle()
drawer.shape("arrow")
drawer.color("blue")

screen = Screen()

def turn_left():
    global drawer
    drawer.left(15)

def turn_right():
    global drawer
    drawer.right(15)

def paint():
    global drawer
    drawer.forward(10)

screen.listen()
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")
screen.onkey(paint, "Up")


screen.exitonclick()