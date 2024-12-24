import requests
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/fatch_name",methods=["GET","POST"])
def fatch_name():
    if requests.methods == "POST":
        name = requests.fatch_name('name')
        return f"your name is {name}"
    return render_template("name.html")


if __name__ == "__main__":
    app.run(debug = True)