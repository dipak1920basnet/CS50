from cs50 import get_float
changes_list = {'quarters' : 25,
                'dimes'    : 10,
                'nickles'  : 5,
                'pennies'  : 1}
# changes = [25,10,5,1]
while True:
    get_changes = get_float("change owed: ")
    get_changes = int(get_changes*100)
    if get_changes < 0:
        continue
    else:
        break
count_changes = 0
while get_changes != 0:
    if get_changes <= 0:
       break
    else:
        for i in changes_list.values():
            if i <= get_changes:
                if get_changes <= 0:
                    break
                get_changes = get_changes-i
                count_changes += 1
                break
print(count_changes)




