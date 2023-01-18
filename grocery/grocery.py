import array

array = []
while True:
    try:
        grocery = input("")
        array.append(grocery)
    except EOFError:
        array.reverse()
        set = sorted(set(array))
        print("\n")
        for i in set:
            print(array.count(i), i.upper())
        break

