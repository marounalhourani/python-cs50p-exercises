def main():
    hour = input("what is the time? ")
    hour = convert(hour)

    if(7<=hour<=9):
        print("breakfast time")
    elif(12<=hour<=13):
        print("lunch time")
    elif(18<=hour<=19):
        print("dinner time")

def convert(time):
    hour, minutes = time.split(":")
    hour = int(hour)
    minutes= float(minutes) * 0.01
    minutes = minutes * (10/6)
    return hour + minutes



if __name__ == "__main__":
    main()
