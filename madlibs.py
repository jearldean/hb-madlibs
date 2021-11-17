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

    game_or_no = request.args.get("game_on")

    if game_or_no == "on":
        return render_template("madlib_form.html", player=player)
    return render_template("goodbye.html", person=player, compliment=compliment)


@app.route("/madlibs")
def show_madlibs_answer():

    color_from_form = request.args.get("color")
    noun_from_form = request.args.get("noun")
    person_from_form = request.args.get("person")
    adjective_from_form = request.args.get("adjective")

    display_madlib = choice(["madlibs1.html", "madlibs2.html", "madlibs3.html"])
    return render_template(display_madlib, color=color_from_form, noun=noun_from_form, person=person_from_form, adjective=adjective_from_form)


if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0")
