while True:
    try:
        a, b = map(int, input("Fraction: ").split("/", 1))

        if a <= b and b != 0:
            x = a / b * 100
            if x <= 1:
                print("E")
                break
            elif x >= 99:
                print("F")
                break
            else:
                print(f"{x:.0f}%")
                break
    except(ValueError, ZeroDivisionError):
        pass

