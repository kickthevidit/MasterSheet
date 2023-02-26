import re
import PyPDF2 
from sympy.parsing.latex import parse_latex

import io
import pdfminer
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfdevice import PDFDevice

import pytesseract
import cv2
from pdfminer.high_level import extract_text_to_fp

# Define a function to extract text from a PDF file
def extract_text_from_pdf(pdf_file_path):
    output_string = io.StringIO()
    with open(pdf_file_path, 'rb') as pdf_file:
        extract_text_to_fp(pdf_file, output_string)
    return output_string.getvalue()

# Define a function to extract text from an image
def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(image)
    return text


# Define a function to extract text from a PDF file
# def extract_text_from_pdf(pdf_file_path):
#     with open(pdf_file_path, 'rb') as pdf_file:
#         parser = PDFParser(pdf_file)
#         document = PDFDocument(parser)
#         rsrcmgr = PDFResourceManager()
#         retstr = io.StringIO()
#         laparams = LAParams()
#         device = TextConverter(rsrcmgr, retstr, laparams=laparams)
#         interpreter = PDFPageInterpreter(rsrcmgr, device)
#         for page in PDFPage.create_pages(document):
#             interpreter.process_page(page)
#         text = retstr.getvalue()
#         device.close()
#         retstr.close()
#         return text

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


def main():
    filename = "./tests/447.png"
    parsed = extract_text_from_image(filename)
    #parsed = parse_pdf(filename)
    chunks = split_contents(parsed)
    print(chunks)

main()