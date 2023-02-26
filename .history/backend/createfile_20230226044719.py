from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def write_to_txt(contents):
    with open("txt_output.txt", "w") as fo:
        fo.write(contents)

def txt_to_pdf(txt_file_path, pdf_file_path): # returns a pdf file
    pdfmetrics.registerFont(TTFont('SF', 'sf.ttf'))
    c = canvas.Canvas(pdf_file_path, pagesize=letter)
    with open(txt_file_path, 'r') as f:
        txt = f.read().splitlines()
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
        
###
# import convertpdf as cpdf
# def main():
#     file = open("./tests/Calculus.pdf", "rb")
#     print("Started parsing...")
#     text = cpdf.parse_pdf(file)
#     write_to_txt(text)
#     print("Write to txt successful")
#     txt_to_pdf("txt_output.txt", "pdf_output.pdf").save()
#     print("Write to pdf successful")
    
# main()