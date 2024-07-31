from cs50 import get_int
def main():
    while True:
        heights = get_int("Height: ")
        if heights not in range(1,9):
            continue
        else:
            print_heights(heights)
            break
def print_heights(x):
    for i in range(1,x+1):
        one = " "*(x-i)+("#"*i)
        print(one)
if __name__ == "__main__":
    main()

