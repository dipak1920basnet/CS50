import random
while True:
    try:
        get_level = int(input("Level: "))
    except ValueError:
        continue
    else:
        if get_level < 1:
            continue
        else:
            break
t = random.randint(1,get_level)
while True:
    try:
        Guess = int(input("Guess: "))
    except ValueError:
        continue
    else:
        if Guess < 1:
            continue
        if Guess == t:
            print("Just right!")
        elif Guess < t:
            print("Too small!")
            continue
        else:
            print("Too large!")
            continue
        break


