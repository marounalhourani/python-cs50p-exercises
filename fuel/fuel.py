# fraction = input("input a fraction X/Y: ")
# index = fraction.index("/")
# X = fraction[0: index]
# length = len(fraction)
# Y = fraction[index + 1: length]

while True:
    try:

        fraction = input("input a fraction X/Y: ")
        index = fraction.index("/")
        X = fraction[0: index]
        length = len(fraction)
        Y = fraction[index + 1: length]
        X = int(X)
        Y = int(Y)
        if(X > Y):
            pass
        elif (0.99 <= (X/Y) <= 1):
            print("F")
            break
        elif(0 <= (X/Y) <=0.01):
            print("E")
            break
        else:
            print ("{:.0%}".format(X/Y))
            break
    except ValueError:
        print("Error")
    except ZeroDivisionError:
        print("Cannot divide by zero")


