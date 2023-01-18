math = input("enter an operation:x y z:  \n").split()
x = int(math[0])
y= math[1]
z = int(math[2])


if(y == "+"):
    result = float(int(x)+int(z))
    print(result)
elif(y=="-"):
    result = float(int(x)-int(z))
    print(result)
elif(y=="*"):
    result = float(int(x)*int(z))
    print(result)
elif(y=="/"):
    result = float(int(x)/int(z))
    print(result)
else:
    print("error")


