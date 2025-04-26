from flask import Flask
import time

app = Flask(__name__)


def adv_logger(func):
    def wrapper(*args):
        print(f"You called {func.__name__}{args}")
        result = func(*args)
        print(f"It returned: {result}")
        return result
    return wrapper


def timer(func):
    def wrapper():
        before_time = time.time()
        result = func()
        after_time = time.time()
        print(f"{func.__name__} run speed: {after_time - before_time}s")
        return result
    return wrapper


def title(func):
    def wrapper():
        return f"<h1>{func()}</h1>"
    return wrapper


@timer
@title
def content():
    return "Hello World"


@app.route("/")
def hello_world():
    return content()


if __name__ == "__main__":
    app.run()

