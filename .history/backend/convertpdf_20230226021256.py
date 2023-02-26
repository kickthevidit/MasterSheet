import re
import io
import pytesseract
import cv2
import pdfminer
import PyPDF2

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from sympy.parsing.latex import parse_latex


def parse_math_equations(text):
    pattern = r'(?i)\b((d|dx|dy|dt)\s*)?([a-z]+|\d+)\s*(=|>|<|>=|<=|!=)\s*([a-z]+|\d+|\([\s\S]*?\))'
    matches = re.findall(pattern, text)
    equations = []
    for match in matches:
        lhs = match[0]
        rhs = match[4]
        equation = f'${lhs} {match[3]} {rhs}$'
        equations.append(equation)
    return equations

def extract_text_from_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(thresh)
    return text

def parse_pdf(pdf_file_path):
    with open(pdf_file_path, 'rb') as pdf_file:
        parser = PDFParser(pdf_file)
        document = PDFDocument(parser)
        rsrcmgr = PDFResourceManager()
        retstr = io.StringIO()
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        for page in PDFPage.create_pages(document):
            interpreter.process_page(page)
        text = retstr.getvalue()
        device.close()
        retstr.close()
        return text

def split_contents(contents):
    content_arr = []
    tokens = 0
    content = ""
    for c in contents:
        if tokens >= 5000:
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
    filename = "./tests/ottoman.pdf"
    parsed = parse_pdf(filename)
    print(parsed)
    chunks = split_contents(parsed)
    print(chunks[1])

main()