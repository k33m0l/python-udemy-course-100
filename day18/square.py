from turtle import Turtle, Screen

drawer = Turtle()
drawer.shape("arrow")
drawer.color("blue")

for _ in range(4):
    drawer.forward(100)
    drawer.left(90)

Screen().exitonclick()