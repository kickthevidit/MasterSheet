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
        txt = f.readlines()
    
    # Set the font size and text color
    c.setFont("Helvetica", 12)
    c.setFillColorRGB(0, 0, 0)
    
    # Set the initial y-coordinate to start writing the text
    y = 750
    
    # Write each line of the text to the PDF file
    for line in txt:
        c.drawString(100, y, line)
        y -= 20  # Move the y-coordinate down by 20 units for each line
    
    # Save the PDF file
    c.save()
Here, we use the readlines() method instead of read() to read the text file, which returns a list of lines in the file. We then loop through each line and use the drawString() method to write the line to the PDF file. The y variable keeps track of the y-coordinate of the current line and is moved down by 20 units for each line to account for line breaks.

You can then call this function by passing the paths to your text and PDF files as arguments:

python
Copy code
txt_to_pdf('my_text_file.txt', 'my_pdf_file.pdf')
This will create a new PDF file named my_pdf_file.pdf that contains the contents of your text file, accounting for line breaks.







        
def main():
    file = open("./tests/graph_theory.pdf", "rb")
    print("Started parsing...")
    text = cpdf.parse_pdf(file)
    write_to_txt(text)
    print("Write to txt successful")
    txt_to_pdf("mastersheet.txt", "mastersheet.pdf")
    
main()