grocery_list = {}
while True:
    try:
        grc = input().upper()
        if grc in grocery_list:
            grocery_list[grc] += 1
        else:
            grocery_list[grc] = 1
    except EOFError:
        break
grocery_list = dict(sorted(grocery_list.items()))
for x , y in grocery_list.items():
    print(f"{y} {x}")
