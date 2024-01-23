def main():
    t = input("What time is it? ")
    x = [
        {"m":"breakfast time","s": 7, "e" : 8},
        {"m":"lunch time","s": 12, "e" : 13},
        {"m":"dinner time","s": 18, "e" : 19}
    ]
    ti = convert(t)
    for i in x:
        if ti <= i["e"] and ti >= i["s"]:
            print(i["m"])

def convert(time):
    z = 0.0
    if time.endswith(" a.m"):
        time = time.strip(" a.m")
    elif time.endswith(" p.m"):
        time = time.strip(" p.m")
        z = 12

    h , m = time.split(":")
    r = int(h) + float(int(m) / 60) + z

    return r

if __name__ == "__main__":
    main()
