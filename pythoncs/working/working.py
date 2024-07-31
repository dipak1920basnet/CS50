# # import re
# # import sys


# # def main():
# #     print(watch(input("Hours: ")))


# # def watch(s):
# #     new = re.search("^[0-9]{1}([0-2]{1})?:?([0-6]{1}[0-9]{1})?AM to [0-9]{1,2}:?([0-6]{1}[0-9]{1})? PM$",s)
# #     if new:
# #         return "Valid"
# #     else:
# #         return "Invalid"

# # if __name__ == "__main__":
# #     main()


# import re
# import sys

# def main():
#     print(watch(input("Hours: ")))


# def watch(s):
#     # validate = re.search("^[0-9]{1}([0-2]{1})?$",s)
#     validate = re.search("^(([0-9]{1}([0-2]{1})?(:)?([0-5]{1}[0-9]{1})?) (AM|PM){1}) (to){1} (([0-9]{1}([0-2]{1})?(:)?([0-5]{1}[0-9]{1})?) (AM|PM){1})$",s)
#     if validate:
#         # return "Valid"
#         start = validate.group(1)
#         end = validate.group(8)
#         a = validate.group(2)
#         b = validate.group(9)
#         if start.endswith("PM"):
#             if ":" in a:
#                 first, last = a.split(":")
#                 first = int(first) + 12
#                 a = f"{first}:{last} "
#             else:
#                 a = int(a) + 12
#                 a = f"{a}:00"

#         if end.endswith("PM"):
#             if ":" in b:
#                 first, last = b.split(":")
#                 first =  int(first) + 12
#                 b = f"{first}:{last}"
#             else:
#                 b = int(b) + 12
#                 b = f"{b}:00"
#         a = add_zero(a)
#         b = add_zero(b)
#         return f"{a} to {b}"
#     else:
#         raise ValueError
#         # return "Invalid"

# def add_zero(a):
#     # a = f"0{a}"
#     if len(str(a))==1:
#         a = f"0{a}"
#     if ":" not in a:
#         a = f"{a}:00"

#     return a

# # def add_back(a):
# #     ...

# if __name__ == "__main__":
#     main()


import re
import sys

def main():
     print(convert(input("Hours: ")))

def convert(s):
    t = r"(1[0-2]|0?[0-9]):?([0-5][0-9])? (AM|PM)"
    if k := re.search((r"^" + t + r" to " + t + r"$"),s):
    #     print(f"Valid: {k.groups()}")
    #     # print(f"Valid: {k.group(8)}")
    # else:
    #     print("Invalid")
        before = watch(k.group(1),k.group(2),k.group(3))
        after = watch(k.group(4),k.group(5),k.group(6))
    else:
        raise ValueError
    return f"{before} to {after}"


def watch(h,m,i):
    if i == "AM":
        if h == "12":
            h = "00"
        else:
            pass
    else:
        if h !="12":
            h = int(h) + 12
        else:
            pass

    if m == None:
        m = "00"
    if int(h) < 10:
        h = f"{int(h):02}"
    return f"{h}:{m}"


if __name__ == "__main__":
    main()
