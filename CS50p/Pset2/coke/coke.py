price = 50
get = 0

while get < price:
    print(f"Amount Due: {price - get}")
    x = int(input("Insert Coin: "))
    if x == 5 or x == 10 or x == 25:
        get += x
    else:
        continue
print(f"Change Owed: {get - price}")
