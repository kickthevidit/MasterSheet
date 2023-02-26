import os
import openai
from flask import Flask, redirect, render_template, request, url_for, abort
from werkzeug.utils import secure_filename
from markupsafe import escape
 
from backend import convertpdf

app = Flask(__name__)
openai.api_key = os.getenv("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")

UPLOAD_FOLDER = "tmp"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config['UPLOAD_EXTENSIONS'] = ['.pdf']


@app.route("/", methods = ["GET", "POST"])
def hello(name = "Anonymous"):
    if request.method == "POST":
        f = request.files['file']
        filename = secure_filename(f.filename)
        if filename != '':
            ext = os.path.splitext(filename)[1]
            if ext not in app.config['UPLOAD_EXTENSIONS']:
                abort(400)
            f.save(app.config['UPLOAD_FOLDER'] + filename)
            return convertpdf.parse_pdf(app.config['UPLOAD_FOLDER'] + filename)
    return "Hello, World!"

@app.route("/generate", methods=("GET", "POST"))
def generate():
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=insert_prompt(prompt),
            temperature=0.5,
        )
        return render_template("index.html", prompt=prompt, response=response.choices[0].text)
    return render_template("index.html")


