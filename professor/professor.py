import random

def main():
    list_equation = []
    list_equation_sol = []
    lev = get_level()
    user_input_list = []
    correct = []
    for x in range(10):
        equation = str(generate_integer(lev)) + " + " + str(generate_integer(lev))
        solution = eval(equation)
        list_equation.append(equation)
        list_equation_sol.append(solution)
        for y in range(3):
            try:
                print(equation ,"=", end = " ")
                user_inp = int(input())
                if user_inp == list_equation_sol[x]:
                    user_input_list.append(user_inp)
                    correct.append("correct")
                    break
                else:
                    print("EEE")
                    continue
            except:
                    print("EEE")

        if y == 2:
            print(equation ,"=", list_equation_sol[x])

    print("score:", len(correct))


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                return level
                break
            else:
                pass
        except:
            pass

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10,99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()