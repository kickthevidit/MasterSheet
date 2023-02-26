import os
import openai
import PyPDF2 as pypdf
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


def summarize_pdf(folder_path):
    model_engine = "text-davinci-003"
    max_tokens = 1024
    for file_name in os.listdir(folder_path):
        if file_name.endswith(".pdf"):
            # Read PDF document
            with open(os.path.join(folder_path, file_name), "rb") as f:
                pdf_reader = PyPDF2.PdfReader(f)
                contents = ""
                for page in pdf_reader.pages:
                    contents += page.extract_text()
            # Generate summary using GPT-3
            prompt = f"Please summarize the following document: {contents}"
            response = openai.Completion.create(
                engine=model_engine,
                prompt=prompt,
                max_tokens=max_tokens
            )
            summary = response.choices[0].text.strip()
            
            # Output summary
            print(f"Summary of {file_name}:")
            print(summary)

def parse_equatiosn(folder)