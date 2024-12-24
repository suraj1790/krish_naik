from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to flask course"

if __name__ == "__main__":
    app.run(debug=True,port=5001)