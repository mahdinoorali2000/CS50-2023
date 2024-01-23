import random

ran = {
    1: [0 , 9],
    2: [10 , 99],
    3: [100 , 999]
}

def main():
    digit = get_level()
    T = 0

    for reg in range(10):
        x = generate_integer(digit)
        y = generate_integer(digit)
        F = 0

        while True:
            try:
                ans = int(input(f"{x} + {y} = "))

                if ans != (x + y) and F < 2:
                    F += 1
                    print("EEE")
                elif ans != (x + y) and F == 2:
                    print(f"{x} + {y} = {x + y}")
                    break
                else:
                    T += 1
                    break

            except (ValueError, EOFError):
                pass

    print(f"Score: {T}")

def get_level():
    while True:
        try:
            x = int(input("Level: "))
            if x <= 3 and x >=1:
                return x
        except ValueError:
            pass

def generate_integer(level):

    h = ran[level][1]
    l = ran[level][0]

    return random.randrange(l , h + 1)

if __name__ == "__main__":
    main()
