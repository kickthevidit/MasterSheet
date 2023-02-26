import createsheet as cp
import convertpdf as cpdf

# we want to take the text output from parse_pdf and write it to a .txt file

def write_to_txt(contents):
    with open("mastersheet.txt", "w") as fo:
        fo.write(contents)
        
def main():
    file = open("./tests/otto.pdf", "rb")
    print("Reached here")
    text = cpdf.parse_pdf(file)
    write_to_txt(text)
    print("Write to txt successful")
    
main()