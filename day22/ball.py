from turtle import Turtle

STEP = 10
DEFAULT_SPEED = 0.1

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.x_move = STEP
        self.y_move = STEP
        self.move_speed = DEFAULT_SPEED

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def detect_collision_bounce_wall(self):
        if self.ycor() > 280 or self.ycor() < -280:
            self.y_move *= -1

    def reset_pos(self):
        self.move_speed = DEFAULT_SPEED
        self.goto(0, 0)
        self.x_move *= -1