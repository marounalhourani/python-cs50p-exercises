import random

while True:
    try:
        level = int(input("Level: "))
        if level > 1:
            n = random.randint(1 , level)
            break
        else:
            continue
    except:
        continue

while True:
    try:
        guess = int(input("Guess: "))
        if guess == n:
            print("Just right!")
            break
        elif guess < n:
            print("Too small!")
            continue
        elif guess > n:
            print("Too large!")
            continue
    except:
        pass