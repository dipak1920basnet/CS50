def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) not in range(2, 7) or s.startswith("0") or (s.isalnum() == False):
        return False
    else:
        if s[:2].isalpha():
            for i in s[2:]:
                if i.isdigit():
                    t = s.index(i)
                    k = s[t:]
                    if k.isdigit() and (k.startswith("0") is False):
                        return True
                    else:
                        return False
            else:
                return True
        else:
            return False


main()
