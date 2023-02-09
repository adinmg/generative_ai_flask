import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
#openai.api_key = os.environ["OPENAI_API_KEY"] # Uncomment this line if you have an environment API key
#openai.api_key = "replace" # Uncomment and replace with your API key
openai.api_key_path = ".\key.txt" # Uncomment if you have a file with your API key

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        animal = request.form["animal"]
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=generate_prompt(animal),
            temperature=0.6, 
        )
        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)


def generate_prompt(animal):
    return """Suggest three names for an animal that is a superhero.
Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        animal.capitalize()
    )