import io
import pdfminer
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument

def parse_pdf(pdf_file):
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
    sections = 1
    length = len(contents)
    while length / sections >= 5000:
        sections += 1
    for c in contents:
        if tokens >= length / sections:
            content_arr.append(content)
            content = ""
            tokens = 0
        else:
            content += c
            tokens += 1
    
    content_arr.append(content)
    return content_arr


