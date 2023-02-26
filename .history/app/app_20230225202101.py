import os
import openai
import re
import PyPDF2 as pypdf
from sympy.parsing.latex import parse_latex
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
            prompt=chatgpt_prompt(prompt),
            temperature=0.6,
        )
        return render_template("index.html", prompt=prompt, response=response.choices[0].text)
    return render_template("index.html")


def chatgpt_prompt(text):
    return """Limiting it to 1 page, summarize this piece of text
    """.format(text.capitalize())

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
            math_strings = re.findall(r"\$.*?\$", text) # parsing using regex/laTEX library to get math equations
            for math_string in math_strings:
                try:
                    equation = parse_latex(math_string)
                    equations.append(equation)
                except:
                    pass
    return equations

