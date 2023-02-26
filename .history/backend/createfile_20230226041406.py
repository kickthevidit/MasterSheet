import createsheet as cp
import convertpdf as cpdf

# we want to take the text output from parse_pdf and write it to a .txt file

def write_to_txt(contents):
    with open("mastersheet.txt", "w") as fo:
        fo.write(contents)

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def txt_to_pdf(txt_file_path, pdf_file_path):
    # Create a new PDF file
    c = canvas.Canvas(pdf_file_path, pagesize=letter)
    
    # Open the text file and read its contents
    with open(txt_file_path, 'r') as f:
        txt = f.read()
    
    # Set the font size and text color
    c.setFont("Helvetica", 12)
    c.setFillColorRGB(0, 0, 0)
    
    # Write the text to the PDF file
    c.drawString(100, 750, txt)
    
    # Save the PDF file
    c.save()
        
def main():
    file = open("./tests/ottoman.pdf", "rb")
    print("Started parsing...")
    text = cpdf.parse_pdf(file)
    write_to_txt(text)
    print("Write to txt successful")
    
main()