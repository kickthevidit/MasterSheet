import createsheet as cp
import convertpdf as cpdf

# we want to take the text output from parse_pdf and write it to a .txt file

def write_to_txt(contents):
    with open("mastersheet.txt", "w") as fo:
        fo.write(contents)
        
def main():
    file = open("./tests/ottoman.pdf", "rb")
    print("ff")
    text = cpdf.create_sheet(file)
    write_to_txt(text)
    
main()