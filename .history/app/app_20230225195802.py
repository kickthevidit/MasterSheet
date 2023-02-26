import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("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")


@app.route("/", methods=("GET", "POST"))
def index():
    return "This server works"

@app.route("/generate", methods=("GET", "POST"))
def generate():
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(p),
            temperature=0.6,
        )
        return render_template("index.html", prompt=prompt, response=response.choices[0].text)
    return render_template("index.html")


def generate_prompt(text):
    return """Suggest three names for an animal that is a superhero.
Animal: Cat
Names: Captain Sharpclaw, Agent Fluffball, The Incredible Feline
Animal: Dog
Names: Ruff the Protector, Wonder Canine, Sir Barks-a-Lot
Animal: {}
Names:""".format(
        text.capitalize()
    )