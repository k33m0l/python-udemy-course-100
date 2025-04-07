import pandas
import turtle

screen = turtle.Screen()
screen.title("Blind map")
screen.setup(800, 600, 0, 0)

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
correct_states = []

while len(correct_states) < 50:
    answer_state = screen.textinput(title=f"{len(correct_states)}/50 state correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in states and answer_state not in correct_states:
        print(f"{answer_state} is correct")
        correct_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_data.state.item(), align="center")

missing_states = [state for state in states if state not in correct_states]
new_data = pandas.DataFrame(missing_states)
new_data.to_csv("states_to_learn.csv")

screen.exitonclick()