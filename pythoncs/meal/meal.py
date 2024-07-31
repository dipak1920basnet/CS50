def main():
    time = input("What time is it? ")
    t = str(convert(time))
    if t.startswith("7"):
        print("breakfast time")
    elif t.startswith("12") or t.startswith("13"):
        print("lunch time")
    elif t.startswith("18"):
        print("dinner time")


def convert(time):
    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)
    if hour > 23:
        pass
    elif minute > 60:
        pass
    else:
        minute = (minute/60)
        return (hour + minute)

if __name__ == "__main__":
    main()
