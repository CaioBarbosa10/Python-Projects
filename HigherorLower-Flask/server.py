from flask import Flask
import random

app = Flask(__name__)

random_number = random.randint(0,9)

@app.route("/<int:guess>")
def check(guess):
    if guess < random_number:
        return "<h1 style='color: purple'>The number is too low </h1>"\
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'/>"
    elif guess > random_number:
        return "<h1 style='color: blue'>The number is too High </h1>"\
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'/>"
    else:
        return "<h1 style ='color: green'> You found the correct number </h1>"\
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'/>"



@app.route("/")
def home():
    return "<h1>Guess a number between 0 and 9</h1>"\
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'/>"



if __name__ == "__main__":
    app.run(debug=True)
