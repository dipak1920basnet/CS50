def main():
    while True:
        m, n = fraction()
        try:
            t = int(round((m / n) * 100))
        except ZeroDivisionError:
            continue
        else:
            if t <= 1:
                print("E")
                break
            elif t >= 99:
                print("F")
                break
            else:
                print(f"{t}%")
                break
    # print(m,n)


def fraction():
    while True:
        t = input("Fraction: ")
        if "/" not in t:
            continue
        else:
            x, y = t.split("/")

        try:
            x = int(x)
            y = int(y)
        except ValueError:
            continue
        else:
            if x > y:
                continue
            else:
                return (x, y)


if __name__ == "__main__":
    main()
