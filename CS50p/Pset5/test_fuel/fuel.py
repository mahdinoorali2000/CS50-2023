def main():
    while True:
        try:
            reg= input("Fraction: ")
            print(gauge(convert(reg)))
            break
        except(ValueError, ZeroDivisionError):
            pass

def convert(fraction):
    if "/" in fraction:
        x , y = fraction.split("/")
    else:
        raise ValueError("not regular")

    if x.isdigit() and y.isdigit():
        if int(x) <= int(y) and int(y) > 0:
            return int(x) / int(y) * 100
        else:
            raise ZeroDivisionError("x < y !!!")
    else:
        raise ValueError("x and y not integer")


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()
