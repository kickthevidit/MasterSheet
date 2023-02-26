from .createsheet import *

# we want to take the text output from parse_pdf and write it to a .txt file

def write_to_txt(contents):
    with open("tmpmastersheet.txt", "w") as fo:
        fo.write(contents)
