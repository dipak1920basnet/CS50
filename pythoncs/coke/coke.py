accepted_coin = [25, 10, 5]
Due_amount = 50
while True:
    print(f"Amount Due: {Due_amount}")
    get_coin = int(input("Insert Coin: "))
    if get_coin not in accepted_coin:
        continue
    else:
        Due_amount = Due_amount - get_coin
        if Due_amount <= 0:
            change = 0 - Due_amount
            print(f"Change Owed: {change}\n")
            break
