import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/index")
def index():
    return render_template('index.html')

@app.route("/about")
def about():
    return render_template("about.html")

# @app.route("/form",methods=["POST","GET"])
# def form():
#     if requests.method == "POST":
#         name = requests.form('name')
#         return f"name is : {name}"
#     return render_template("form.html")

@app.route("/sucess/<int:score>")
def sucess(score):
    # return f"gaining mark is {score}"

    if score >= 50:
        return f"You have passed"
    else:
        return "You have to failed"




if __name__ == "__main__":
    app.run(debug=True)