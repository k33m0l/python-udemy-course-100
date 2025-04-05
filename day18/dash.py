from turtle import Turtle, Screen

drawer = Turtle()
drawer.shape("arrow")
drawer.color("blue")

for n in range(1, 30):
    drawer.forward(10)
    if n % 2 == 0:
        drawer.pendown()
    else:
        drawer.penup()
        

Screen().exitonclick()