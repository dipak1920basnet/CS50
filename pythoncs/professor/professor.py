

import random


def main():
    count_mistake = 0
    score = 0
    level = get_level()
    for i in range(10):
        a = generate_integer(level)
        b = generate_integer(level)
        answer = a + b
        while True:
            make_guess = int(input(f"{a} + {b} = "))
            if make_guess != answer:
                count_mistake += 1
                print("EEE")
                if count_mistake==3:
                    print(f"{a} + {b} = {answer}")
                    break
            else:
                score += 1
                break
    print(f"Score: {score}")


# Get the level
def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in range(1,4):
                raise ValueError
        except ValueError:
            continue
        else:
            # else:
            return level

# Randomly generate 10 math problem formatted as X+Y= , both X and Y are non negative integer
def generate_integer(level):
    if level == 1:
        return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)


if __name__ == "__main__":
    main()
