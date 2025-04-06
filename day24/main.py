from turtle import Screen
from snake import Snake
from food import Food_Spawner
from score import ScoreBoard
import time

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=600, height=600, startx=0, starty=0)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
spawner = Food_Spawner(WIDTH, HEIGHT)
score = ScoreBoard(HEIGHT)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

def is_wall_hit(pos, limit):
    return pos >= limit / 2 or pos <= -(limit / 2)

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with food
    if snake.distance(spawner.get_current_pos()) < 20:
        score.add_score()
        snake.grow()
        spawner.move_current()

    # Collision with wall
    head_pos = snake.get_head_pos()
    if is_wall_hit(head_pos[0], WIDTH) or is_wall_hit(head_pos[1], HEIGHT):
        game_on = False
        score.game_over()
    
    # Collision with tail
    for segment in snake.segments[1:]:
        if snake.distance(segment.turtle.pos()) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()