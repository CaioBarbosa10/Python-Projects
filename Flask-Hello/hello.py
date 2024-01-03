from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "bye"

@app.route("/username/<name>")
def greet(name):
    return f"hello {name}"

if __name__ == "__main__":
    app.run(debug=True)