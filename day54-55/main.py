from flask import Flask
import random

RANDOM_NUMBER = random.randint(1, 10)
app = Flask(__name__)


@app.route("/")
def default_route():
    return "<h1>Number quesser game</h1><p>Type a number after a / in the URL bar to guess a number</p>"


@app.route("/<int:number>")
def guess_number(number: int):
    if number < RANDOM_NUMBER:
        return "<h1>Too low, try again!</h1></br><img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    if number > RANDOM_NUMBER:
        return "<h1>Too high, try again!</h1></br><img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h1>You found me!</h1></br><img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"


if __name__ == "__main__":
    app.run()
