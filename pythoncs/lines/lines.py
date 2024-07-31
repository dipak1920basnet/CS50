import sys
def main():
    if len(sys.argv) != 2:
        if len(sys.argv)> 2:
            sys.exit("Too many command line arguments")
        else:
            sys.exit("Too few command line arguments")
    else:
        t = count_lines()
        print(t)

def count_lines():
    try:
        if sys.argv[1].endswith(".py"):
            count = 0
            with open(f"{sys.argv[1]}","r") as file:
                lines = file.readlines()
            for line in lines:
                if line.strip() == "":
                    pass
                elif line.strip().startswith("#"):
                    pass
                else:
                    count +=1
            return (count)

        else:
            sys.exit("Not a Python file")
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()


