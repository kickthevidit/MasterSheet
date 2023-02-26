import re
import PyPDF2
from sympy.parsing.latex import parse_latex

def parse_pdf(filename):
    contents = ""
    model = "text-davinci-003"
    if filename.endswith(".pdf"):
        pdf = open(filename,'rb')
        pdfReader = PyPDF2.PdfReader(pdf)
        for page in pdfReader.pages:
            contents += page.extract_text()
    return contents

def split_contents(contents):
    content_arr = []
    tokens = 0
    content = ""
    for c in contents:
        if tokens >= 4000:
            content_arr.append(content)
            content = ""
            tokens = 0
        else:
            content += c
            tokens += 1
    return content_arr

def get_equations(filename):
    equations = []
    if filename.endswith(".pdf"):
        pdf = open(filename,'rb')
        pdfReader = PyPDF2.PdfReader(pdf)
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