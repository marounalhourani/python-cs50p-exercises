answer = input("What is the answer to Great Question of Life, the Universe and Everything: ")

if ( answer.lower().strip() == "42" or answer.lower() == "forty-two" or answer.lower() == "forty two"):
    print("Yes")
else:
    print('No')