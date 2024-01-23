import re
mon = [
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
    "December"
]

while True:
    try:
        dt = input("Date: ")
        if re.findall("[a-zA-Z]*,", dt) and re.findall("^[a-zA-Z]", dt):
            m, d, y = dt.split(" ")
            d = int(d.strip(", "))
            if m.title() in mon and d <= 31 and d >= 1:
                m = mon.index(m) + 1
                print(f"{y}-{m:02}-{d:02}")
                break

        else:
            m, d, y = map(int,dt.split("/"))

            if d <= 31 and d >= 1 and m <= 12 and m >= 1:
                print(f"{y}-{m:02}-{d:02}")
                break

    except (EOFError,KeyboardInterrupt):
        print()
        quit()

    except:
        pass

