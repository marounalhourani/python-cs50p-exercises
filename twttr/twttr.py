text = input("Input: ")
i = 0
new_text = ""
for i in range(len(text)):
    if (text[i] == "A" or text[i] =="a" or text[i] == "E" or text[i] == "e" or text[i] == "I" or text[i] == "i"
    or text[i] == "O" or text[i] == "o" or text[i] == "U" or text[i] == "u"):
        new_text = new_text

    else:
        new_text += text[i]
print(new_text)

# or text[i] = "E" or text[i] = "e" or
#     text[i] = "I" or text[i] = "i" or text[i] = "O" or text[i] = "o" or text[i] = "U" or text[i] = "u"):