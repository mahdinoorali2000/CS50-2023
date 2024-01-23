import inflect

p = inflect.engine()
n=[]

while True:
    try:
        n.append(input("Name: "))
    except EOFError:
        print(f"\nAdieu, adieu, to {p.join(n)}")
        quit()
