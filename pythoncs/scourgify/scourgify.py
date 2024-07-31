import sys
import csv
def main():
    if len(sys.argv) != 3:
        if len(sys.argv) < 3:
            sys.exit("Too few command line arguments")
        else:
            sys.exit("Too many command line arguments")
    else:
        if not (sys.argv[1].endswith(".csv")) or not (sys.argv[2].endswith(".csv")):
            sys.exit("Not a csv file")
        else:
            try:
                after(sys.argv[1], sys.argv[2])
            except FileNotFoundError:
                sys.exit(f"Could not read {sys.argv[1]}")

def after(a,b):
    actual = []
    with open(a,"r") as file:
        reader = csv.reader(file)
        for line in reader:
            actual.append(line)
    head_row = ["first","last",actual[0][1]]
    with open(b,"w") as file:
        writer = csv.writer(file)
        writer.writerow(head_row)
        for i in range(1,len(actual)):
            k = []
            last, first = actual[i][0].split(",")
            k.append(first.strip())
            k.append(last.strip())
            k.append(actual[i][1])
            writer.writerow(k)

if __name__ == "__main__":
    main()
