import os
import openai
import PyPDF2

openai.api_key = os.getenv("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")

def summarize_text(text):
    response = openai.Completion.create(model="text-davinci-003", prompt=generate_prompt(text),temperature=0.6)
    result=response.choices[0].text
    return result

def generate_prompt(text):
    return """{} \n
    Please summarize the main points and key ideas of the text above. \n
    """.format(text)