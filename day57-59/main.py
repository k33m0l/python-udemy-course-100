from flask import Flask, render_template, request
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

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/send", methods=["POST"])
def send_contact():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]
    message = request.form["message"]
    return "<p>" \
        f"Username: {name}, " \
        f"Email: {email}, " \
        f"Phone number: {phone}, " \
        f"Message: {message}" \
        "</p>"

if __name__ == "__main__":
    app.run()

