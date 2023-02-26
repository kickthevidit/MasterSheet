import createsheet as cp

# we want to take the text output from parse_pdf and write it to a .txt file

def write_to_txt(contents):
    with open("mastersheet.txt", "w") as fo:
        fo.write(contents)
        
def main():
    file = open("./tests/ottoman.pdf", "rb")
    contents = cp.parse_pdf(file)
    print("ff")
    text = create_sheet(contents)
    write_to_txt(contents)
    
main()