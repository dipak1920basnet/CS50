import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # return s.count("um")
    k = r"(\w+)?"
    # t = re.findall((k + r" ?" + r"um" + r" ?" + k),s)
    # t = re.findall(r"(\w+)? ?(um) ?(\w+)?",s)
    # t = re.findall(r"[a-z]* um [a-z]*",s, re.IGNORECASE)
    t = re.findall(r" ?\bum\b ?",s,re.IGNORECASE)
    m = len(t)
    return m
...

if __name__ == "__main__":
    main()
