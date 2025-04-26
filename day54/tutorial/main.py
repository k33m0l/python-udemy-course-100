from flask import Flask

app = Flask(__name__)


def logger_decorator(func):
    def wrapper():
        print("Decorator called")
        func()
    return wrapper


@logger_decorator
def random_function():
    print("Function called")


@app.route("/")
def hello_world():
    random_function()
    return "Hello World"


if __name__ == "__main__":
    app.run()

