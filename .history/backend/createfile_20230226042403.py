import createsheet as cp
import convertpdf as cpdf
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# we want to take the text output from parse_pdf and write it to a .txt file

def write_to_txt(contents):
    with open("mastersheet.txt", "w") as fo:
        fo.write(contents)

def txt_to_pdf(txt_file_path, pdf_file_path):
    # Create a new PDF file
    c = canvas.Canvas(pdf_file_path, pagesize=letter)
    
    # Open the text file and read its contents
    with open(txt_file_path, 'r') as f:
        txt = f.read().replace('\n', ' ')
    
    # Set the font size and text color
    c.setFont("Helvetica", 12)
    c.setFillColorRGB(0, 0, 0)
    
    # Set the initial y-coordinate to start writing the text
    y = 750
    
    # Write the text to the PDF file, accounting for overflow
    for line in txt.split('\n'):
        if y <= 50:
            # If the y-coordinate is less than 50 (i.e., near the bottom of the page),
            # create a new page and reset the y-coordinate to the top
            c.showPage()
            y = 750
        c.drawString(100, y, line)
        y -= 20  # Move the y-coordinate down by 20 units for each line
    
    # Save the PDF file
    #c.save()
    
        
def main():
    file = open("./tests/graph_theory.pdf", "rb")
    print("Started parsing...")
    text = cpdf.parse_pdf(file)
    write_to_txt(text)
    print("Write to txt successful")
    txt_to_pdf("mastersheet.txt", "mastersheet.pdf").save()
    print("Write to pdf successful")
    
main()