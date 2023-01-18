def convert(toreplace):
    toreplace = toreplace.replace(":)","🙂").replace(":(","🙁")
    return toreplace

def main():
    name = input("Enter the text here: ")
    print(convert(name))

main()

