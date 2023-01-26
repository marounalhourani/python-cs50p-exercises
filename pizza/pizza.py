import sys
from tabulate import tabulate
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")
array = []
while True:
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                array.append(row)
            headers = array[0]
            table = array[1:]
            print(tabulate(table, headers, tablefmt="grid"))
            break

    except FileNotFoundError:
        sys.exit("File does not exist")



# if len(sys.argv[1] not in my_files):
#     sys.exit("File does not exist")



