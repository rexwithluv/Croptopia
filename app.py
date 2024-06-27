import flask
import json

app = flask.Flask(__name__)

with open("recipes.json") as f:
    recipes = json.load(f)


@app.route("/", methods=["GET", "POST"])
def index():
    results = []
    if flask.request.method == "POST":
        user_ingredients = flask.request.form.get("ingredients", "").split(",")
        user_ingredients = [ingredient.strip() for ingredient in user_ingredients]

        for recipe in recipes:
            if all(ingredient in recipe["ingredients"] for ingredient in user_ingredients):
                results.append(recipe)



    return flask.render_template("index.html", results=results)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
