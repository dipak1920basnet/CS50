word_month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]
while True:
    Date = input("Date: ").strip()
    if "/" in Date:
        month, day, year = Date.split("/")
        if month.capitalize() in word_month or day.capitalize() in word_month:
            continue
    else:
        month, day, year = Date.split(" ")
        if day.capitalize() in word_month:
            continue
        else:
            Day = ""
            if "," not in day:
                continue
            else:
                for i in day:
                    if i == ",":
                        pass
                    else:
                        Day += i
                if Day.capitalize() in word_month:
                    continue
            day = Day
    if month.capitalize() in word_month:
        month = str(word_month.index(month.capitalize()) + 1)
    if len(month) == 1:
        month = "0" + month
    if len(day) == 1:
        day = "0" + day
    try:
        if int(month) not in range(1, 13) or int(day) not in range(1, 32):
            continue
    except ValueError:
        continue
    else:
        print(f"{year}-{month}-{day}")
        break
