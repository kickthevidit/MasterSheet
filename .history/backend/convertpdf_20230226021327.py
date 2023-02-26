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

def main():
    filename = "./tests/ottoman.pdf"
    parsed = parse_pdf(filename)
    print(parsed)
    chunks = split_contents(parsed)
    print(chunks[1])

main()