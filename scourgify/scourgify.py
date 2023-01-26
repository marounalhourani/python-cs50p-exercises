import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exist("Too many command-line arguments")

    array = []

    while True:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    fullname = row["name"]
                    house = row["house"]
                    last, first = fullname.split(",")
                    array.append({"first":first, "last":last, "house": house})
                break


        except FileNotFoundError:
            sys.exit("Could not read", sys.argv[1])

    with open(sys.argv[2], "w") as output:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(output, fieldnames=fieldnames)
        writer.writeheader()
        for row in array:
            writer.writerow({"first": row["first"].strip(), "last":row["last"].strip(), "house": row["house"].strip()})


if __name__ == "__main__":
    main()