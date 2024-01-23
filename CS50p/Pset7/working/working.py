import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    t = re.findall(
        r"^(?:((?:[0]?[0-9])|(?:[1][0-2])):?([0-5][0-9])? ([AaPp][Mm]) to ((?:[0]?[0-9])|(?:[1][0-2])):?([0-5][0-9])? ([AaPp][Mm]))$",
        s,
        re.IGNORECASE,
    )
    try:
        if t:
            t = [j for j in (t[0]) if j != ""]
            if len(t) == 6:
                h1 = int(t[0])
                m1 = int(t[1])
                ap1 = t[2]
                h2 = int(t[3])
                m2 = int(t[4])
                ap2 = t[5]

                if ap1.lower() == "am":
                    if h1 == 12:
                        ho1 = 00
                    else:
                        ho1 = h1
                else:
                    if h1 == 12:
                        ho1 = 12
                    else:
                        ho1 = h1 + 12
                if ap2.lower() == "am":
                    if h2 == 12:
                        ho2 = 00
                    else:
                        ho2 = h2
                else:
                    if h2 == 12:
                        ho2 = 12
                    else:
                        ho2 = h2 + 12

                return f"{ho1:02}:{m1:02} to {ho2:02}:{m2:02}"
            else:
                h1 = int(t[0])
                ap1 = t[1]
                h2 = int(t[2])
                ap2 = t[3]

                if ap1.lower() == "am":
                    if h1 == 12:
                        ho1 = 00
                    else:
                        ho1 = h1
                else:
                    if h1 == 12:
                        ho1 = 12
                    else:
                        ho1 = h1 + 12
                if ap2.lower() == "am":
                    if h2 == 12:
                        ho2 = 00
                    else:
                        ho2 = h2
                else:
                    if h2 == 12:
                        ho2 = 12
                    else:
                        ho2 = h2 + 12
                return f"{ho1:02}:00 to {ho2:02}:00"
        else:
            raise ValueError
    except ValueError:
        print("ValueError")
        sys.exit(1)


if __name__ == "__main__":
    main()
