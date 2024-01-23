x = input("camelCase: ").strip()
print("snake_case: ",end = "")

for i in x:
    if i.isupper():
        print("_", end = "")
        print(i.lower(), end ="")
    else:
        print(i,end = "")

print()
