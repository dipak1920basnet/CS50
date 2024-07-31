import pyfiglet as fig
import sys
try:
    if len(sys.argv) not in range(0,4):
        sys.exit("Invalid usage")
    else:
        if (sys.argv[1] != "-f") and (sys.argv[1] != "--font"):
            sys.exit("Invalid usage")
        f = fig.Figlet(font=sys.argv[2])
except IndexError:
    sys.exit("Invalid usage")
except fig.FontNotFound:
    sys.exit("Invalid usage")
else:
    # f= fig.Figlet()
    t = input("Input: ")
    print(f"{f.renderText(t)}")

