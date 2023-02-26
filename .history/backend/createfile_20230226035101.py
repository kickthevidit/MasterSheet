import .convertpdf import *

# we want to take the text output from parse_pdf and write it to a .txt file

def write_to_txt(contents):
    with open("mastersheet.txt", "w") as fo:
        fo.write(contents)
        
def main():
    file = open("ottoman.pdf", "rb")
    contents = parse_pdf(file)
    #text = create_sheet(contents)
    write_to_txt(contents)
    