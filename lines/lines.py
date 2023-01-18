import sys
import os

def main():

    my_files = os.listdir()

    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    if sys.argv[1][-3:] != ".py":
        sys.exit("Not a Python file")

    if sys.argv[1] not in my_files:
        sys.exit("File does not exist")

    print(get_number_line(sys.argv[1]))


def get_number_line(path):
    array = []

    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if(line.startswith("#") == False and len(line)!=0):
                array.append(line)

    return len(array)

if __name__ == "__main__":
    main()
