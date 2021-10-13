"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]


@app.route("/")
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game")
def show_madlib_form():
    yes_or_no = request.args.get("game_y_n")
    player = request.args.get("person")
    print (yes_or_no)
    
    if yes_or_no == "Yes":
        return render_template("game.html")
    elif yes_or_no == "No":
        return render_template("#goodbye.html")




@app.route("/madlib")
def show_madlib():
     person = request.args.get("Person")
     color= request.args.get("Color")
     noun = request.args.get("Noun")
     adjective = request.args.get("Adjective")

     adverb = request.args.get("adverb")
     noun2 = request.args.get("noun2")
     city = request.args.get("city")


     return render_template("madlib.html", Person = person, Color = color, Noun = noun, Adjective = adjective, adverb = adverb, noun2 = noun2, city = city)



if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
