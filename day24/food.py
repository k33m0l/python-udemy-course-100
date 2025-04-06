import random
from turtle import Turtle

class Food:
    def __init__(self, pos_x, pos_y):
        self.turtle = Turtle()
        self.turtle.speed("fastest")
        self.turtle.shape("circle")
        self.turtle.fillcolor("blue")
        self.turtle.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.turtle.penup()
        self.turtle.goto(pos_x, pos_y)

    def get_pos(self):
        return self.turtle.pos()
    
    def goto(self, pos_x, pos_y):
        self.turtle.goto(pos_x, pos_y)

class Food_Spawner:
    def get_random_position(self, limit):
        limit -= 40
        screen_limit = int(limit / 2)
        return random.randint(-screen_limit, screen_limit)

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height
        pos_x = self.get_random_position(screen_width)
        pos_y = self.get_random_position(screen_height)
        self.current_food = Food(pos_x, pos_y)

    def get_current_pos(self):
        return self.current_food.get_pos()

    def move_current(self):
        new_x = self.get_random_position(self.screen_width)
        new_y = self.get_random_position(self.screen_height)
        self.current_food.goto(new_x, new_y)