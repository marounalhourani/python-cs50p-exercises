def main():
    print("NRO".isalpha())
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False

    if s[0:1].isalpha() == False:
        return False

    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == "0":
                return False
            else:
                break
        i = i + 1

    x = 1

    while x < len(s):
        if s[x].isnumeric():
            index = x
            break
        x = x + 1

    if 'index' in locals():
        while index < len(s) :
            if s[index].isalpha():
                return False
            index = index + 1




    for c in s:
        if c in ["." , "," , " " , "!", "@", "$", "?"]:
            return False

    return True

main()

