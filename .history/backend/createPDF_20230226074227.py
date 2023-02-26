from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def get_contents(filename):
    with open(filename, 'r') as f:
        txt = f.read().splitlines()
        return txt

def generate_pdf(text, pdf_file_path): # returns a pdf file
    pdfmetrics.registerFont(TTFont('SF', 'sf.ttf'))
    c = canvas.Canvas(pdf_file_path, pagesize=letter)
    txt = text
    c.setFont("SF", 12)
    c.setFillColorRGB(0, 0, 0)
    y = 750
    for line in txt:
        if y <= 50:
            c.showPage()
            y = 750
        c.drawString(100, y, line.replace('\n', ''))
        y -= 20  
    return c
        
### TESTING ###
import convertpdf as cpdf
def main():
    contents = get_contents("test.txt")
    generate_pdf(contents, "./testpdf_output.pdf").save()

main()