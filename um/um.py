import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    pattern = r"\b[,|.]?[u|U][m|M][,|.]?\b"
    return(len([*re.finditer(pattern, s)]))

if __name__ == "__main__":
    main()