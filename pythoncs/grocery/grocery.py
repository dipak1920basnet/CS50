t = {}
while True:
    try:
        get_item = input()
        if get_item not in t:
            t[get_item]=1
        else:
            t[get_item] += 1

    except EOFError:
        break
    except KeyboardInterrupt:
        break

print()      # Sorting the dictionary by key
k = sorted(t)
for i in k:
    print(t[i], i.upper())






