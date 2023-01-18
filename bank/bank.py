greetings = input("Greetings: ").split()

if (greetings[0].lower().replace(",","") == "hello"):
    print("$0")
elif(greetings[0][0].lower() == "h"):
    print("$20")
else:
    print("$100")