import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    validation = re.search(
        r'<iframe.*?src="(http(s)?://)?([w]{3}\.)?youtube\.com/embed/(xvFZjo5PgG0){1}".*?',
        s,
        re.IGNORECASE,
    )
    if validation:
        return f"https://youtu.be/{validation.group(4)}"
    else:
        return


if __name__ == "__main__":
    main()
