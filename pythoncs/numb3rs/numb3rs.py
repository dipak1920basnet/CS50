# import re
# import sys


# def main():
#     print(validate(input("IPv4 Address: ")))


# def validate(ip):
#     if ip.count(".") !=3:
#         return False
#     else:
#         try:
#             hy = ip.split(".")
#             check = True
#             for i in hy:
#                 if int(i) not in range(0,256):
#                     check = False
#                     break
#         except ValueError:
#             return False
#             raise
#         else:
#             return check


# ...


# if __name__ == "__main__":
#     main()


import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r"^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$", ip):
        t = ip.split(".")
        for i in t:
            if int(i) not in range(256):
                return False
        else:
            return True
    else:
        return False


if __name__ == "__main__":
    main()
