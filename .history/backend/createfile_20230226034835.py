from .createsheet import *

# we want to take the text output from parse_pdf and write it to a .txt file

def write_to_txt(contents):
    with open("mastersheet.txt", "w") as fo:
        fo.write(contents)
        
def main():
    file = open("ottom.pdf", "rb")
    contents = parse_pdf(file)
    write_to_txt(contents)
    create_sheet(contents)