def main():

    #as for input
    fra = input("input a fraction X/Y: ")
    per = convert(fra)

    if(isinstance(per, int)):
        print(gauge(per))



def convert(fraction):
    while True:
        try:

            index = fraction.index("/")
            X = fraction[0: index]
            length = len(fraction)
            Y = fraction[index + 1: length]
            X = int(X)
            Y = int(Y)

            if(X/Y <=1):
                return int(round((X/Y) * 100))
            else:
                if(X>Y):
                    raise ValueError()
                    break
                fraction = input("input a fraction X/Y: ")
                pass
        except(ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    if 0 <= percentage <= 1:
        return "E"
    #made the error here
    elif 99 < percentage <=100:
        return "F"
    else:
        return str("{:.0%}".format(percentage/100))





if __name__ == "__main__":
    main()
