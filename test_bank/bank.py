def main():
    gree = input("Greetings: ").split()
    print(value(gree))


def value(greeting):

    if (greeting[0].lower().replace(",","") == "hello"):
        return 0
    elif(greeting[0][0].lower() == "h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()

# returns 0 if that str starts with “hello”,
# 20 if that str starts with an “h” (but not “hello”),
# or 100 otherwise, treating the str case-insensitively.
# You can assume that the string passed to the value function will not contain any leading spaces.
#  Only main should call print.