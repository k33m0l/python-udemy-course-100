from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard
import time

WIDTH = 800
HEIGHT = 600
INIT_POS = 350
BOUNCE_WALL = 320
BALL_MISS = 380

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT, startx=0, starty=0)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

player_left = Paddle(-INIT_POS)
player_right = Paddle(INIT_POS)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_right.up, "Up")
screen.onkey(player_right.down, "Down")
screen.onkey(player_left.up, "w")
screen.onkey(player_left.down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    ball.detect_collision_bounce_wall()
    # Detect collision on right paddle
    if ball.distance(player_right) < 50 and ball.xcor() > BOUNCE_WALL:
        ball.move_speed * 0.9
        ball.x_move *= -1
    # Detect collision on left paddle
    if ball.distance(player_left) < 50 and ball.xcor() < -BOUNCE_WALL:
        ball.move_speed * 0.9
        ball.x_move *= -1

    # Detect right paddle miss
    if ball.xcor() > BALL_MISS:
        scoreboard.l_point()
        ball.reset_pos()

    # Detect left paddle miss
    if ball.xcor() < -BALL_MISS:
        scoreboard.r_point()
        ball.reset_pos()

    if scoreboard.l_score > 1 or scoreboard.r_score > 1:
        game_on = False

screen.exitonclick()