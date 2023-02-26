import os
import openai
import re
import PyPDF2 as pypdf
from sympy.parsing.latex import parse_latex
from flask import Flask, redirect, render_template, request, url_for
from werkzeug.utils import secure_filename


app = Flask(__name__)
openai.api_key = os.getenv("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")

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
            return "Working"

    return "Hello, World!"



@app.route("/", methods=("GET", "POST"))
def index():
    return "This server works"

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

def insert_prompt(text):
    return text

def parse_pdf(filename):
    contents = ""
    model = "text-davinci-003"
    if filename.endswith(".pdf"):
        pdf = open(filename,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdf)
        for page in pdfReader.pages:
            contents += page.extract_text()
    return contents

def get_equations(filename):
    equations = []
    if filename.endswith(".pdf"):
        pdf = open(filename,'rb')
        pdfReader = PyPDF2.PdfFileReader(pdf)
        for page in pdfReader.pages:
            text = page.extract_text()
            pattern = r'\$(.*?)\$'
            math_strings = re.findall(pattern, text) # parsing using regex/laTEX library to get math equations
            for math_string in math_strings:
                try:
                    equation = parse_latex(math_string)
                    equations.append(equation)
                except:
                    pass
    return equations
