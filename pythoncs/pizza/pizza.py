import sys
import csv
from tabulate import tabulate
def main():
    if len(sys.argv) != 2:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        else:
            sys.exit("Too few command-line arguments")
    else:
        try:
            t = sys.argv[1]
            if not t.endswith(".csv"):
                sys.exit("Not a CSV file")
            else:
                k = menu(t)
                print(k)
        except FileNotFoundError:
            sys.exit("File does not exist")


def menu(item_table):
    actual = []
    with open(f"{item_table}","r") as file:
        reader = csv.reader(file)
        for line in reader:
            actual.append(line)
    headers = actual[0]
    return (tabulate(actual[1:], headers=headers, tablefmt="grid"))
if __name__ == "__main__":
    main()
