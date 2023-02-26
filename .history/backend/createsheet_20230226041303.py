import os, io
import openai
from convertpdf import *
from summarizer import *

def create_sheet(file):
    contents = parse_pdf(file)
    sections = split_contents(contents)

    responses = []

    for section in sections:
        responses.append(
            openai.Completion.create(
                model="text-davinci-003",
                prompt=generate_prompt(section),
                temperature=1.0,
                max_tokens=1000)
            )
    text = ""
    for response in responses:
        text = text + response.choices[0].text
    return text



