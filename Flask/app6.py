from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sucess/<int:mark>")
def sucess(mark):
    if mark >= 50:
        res = "Passed"
    else:
        res = "Failed"
    return render_template("sucess.html",result = res)

if __name__ == "__main__":
    app.run(debug=True,port=1)