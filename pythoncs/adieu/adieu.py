import inflect
p = inflect.engine()
names = []
while True:
    try:
        name = str(input("Name: ")).strip()
    except ValueError:
        continue
    except EOFError:
        break
    except KeyboardInterrupt:
        break
    else:
        names.append(name)
names = p.join(names)
print("\nAdieu, adieu, to",names)
