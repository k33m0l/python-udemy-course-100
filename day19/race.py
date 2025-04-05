from turtle import Screen
from racer_turtle import RacingTurtle

colors = ["red", "green", "blue", "yellow", "orange", "purple"]

screen = Screen()
screen.setup(width=500, height=400)

def get_user_bet():
    global screen
    user_bet = screen.textinput("Bet", "Bet on which turtle is going to finish first:").lower()

    if user_bet in colors:
        print("correct color, game starts")
        return user_bet
    else:
        return get_user_bet()

user_bet = get_user_bet()

racers = []
racer_num = 6
for index in range(0, racer_num):
    racers.append(RacingTurtle(colors[index], index))

winner = ""
game_on = True
while game_on:
    for racer in racers:
        if racer.racer.xcor() > 230:
            racers.remove(racer)
            if winner == "":
                winner = racer.color
        if (len(racers) == 0):
            game_on = False
            break
        racer.random_forward()

print(f"Game finished and {winner} won the game!")
if user_bet == winner:
    print("Congratulations!")
else:
    print("You lost")
screen.exitonclick()