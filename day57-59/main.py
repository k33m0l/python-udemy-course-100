from flask import Flask, render_template
import requests

URL="https://api.npoint.io/c790b4d5cab58020d391"
app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(url=URL)
    response = response.json()
    return render_template("index.html", posts=response, is_main=True)

@app.route("/blog/<int:post_num>")
def blog(post_num: int):
    response = requests.get(url=URL)
    response = response.json()
    return render_template("index.html", posts=[blog for blog in response if blog["id"] == post_num], is_main=False)

if __name__ == "__main__":
    app.run()

