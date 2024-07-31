# def main():
#     while True:
#         try:
#             f = input("Fraction: ")
#             k = convert(f)
#             volume = gauge(k)
#             print(volume)
#             break
#         except (ValueError, ZeroDivisionError):
#             pass

# def convert(fraction):
#     try:
#         x, y = fraction.split("/")
#         x = int(x)
#         y = int(y)
#         if y == 0:
#             raise ZeroDivisionError
#         if x > y:
#             raise ValueError
#         t = x / y
#         return int(round((t) * 100))
#     # except (TypeError):
#     #     raise TypeError
#     except (ValueError,ZeroDivisionError):
#         raise
#     # except (ZeroDivisionError):
#     #     raise ZeroDivisionError



# def gauge(percentage):
#     t = percentage
#     if t <= 1:
#         return "E"
#     elif t >= 99:
#         return "F"
#     else:
#         return f"{t}%"


# if __name__ == "__main__":
#     main()


def main():
    try:
        f = input("Fraction")
        t = convert(f)
        gauge(t)
    except (ValueError):
        main()

def convert(fraction):
    try:
        x,y = fraction.split("/")
        x,y = int(x), int(y)
        t = x/y
        k = int(round((t) * 100))
        if k not in range(0,101):
            raise ValueError
        if x > y:
            raise ValueError
        return k
    except ValueError:
        raise
    except ZeroDivisionError:
        raise

def gauge(percentage):
    t = percentage
    if t <= 1:
        return "E"
    elif t >= 99:
        return "F"
    else:
        return f"{t}%"

if __name__ == "__main__":
    main()
