def main():
    word = input("Input: ")
    print(shorten(word))

def shorten(word):
    new_text = ""
    for i in range(len(word)):
        if (word[i] == "A" or word[i] =="a" or word[i] == "E" or word[i] == "e" or word[i] == "I" or word[i] == "i"
        or word[i] == "O" or word[i] == "o" or word[i] == "U" or word[i] == "u"):
            word = word

        else:
            new_text += word[i]
    return new_text


if __name__ == "__main__":
    main()