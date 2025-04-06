from turtle import Turtle 

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
DIRECTION_UP = 90
DIRECTION_DOWN = 270
DIRECTION_LEFT = 180
DIRECTION_RIGHT = 0

class SnakeBody:
    def __init__(self, pos):
        self.turtle = Turtle()
        self.turtle.shape("square")
        self.turtle.fillcolor("white")
        self.turtle.penup()
        self.turtle.goto(pos)

class Snake:
    segments = []
    def __init__(self):
        for pos in START_POS:
            self.segments.append(SnakeBody(pos))

    def move(self):
        global seg
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].turtle.xcor()
            new_y = self.segments[seg_num - 1].turtle.ycor()
            self.segments[seg_num].turtle.goto(new_x, new_y)
        self.segments[0].turtle.forward(MOVE_DISTANCE)

    def grow(self):
        pos = self.segments[-1].turtle.pos()
        self.segments.append(SnakeBody(pos))
    
    def up(self):
        if (self.segments[0].turtle.heading() != DIRECTION_DOWN):
            self.segments[0].turtle.setheading(DIRECTION_UP)

    def down(self):
        if (self.segments[0].turtle.heading() != DIRECTION_UP):
            self.segments[0].turtle.setheading(DIRECTION_DOWN)

    def left(self):
        if (self.segments[0].turtle.heading() != DIRECTION_RIGHT):
            self.segments[0].turtle.setheading(DIRECTION_LEFT)

    def right(self):
        if (self.segments[0].turtle.heading() != DIRECTION_LEFT):
            self.segments[0].turtle.setheading(DIRECTION_RIGHT)

    def distance(self, target):
        return self.segments[0].turtle.distance(target)
    
    def get_head_pos(self):
        return self.segments[0].turtle.pos()