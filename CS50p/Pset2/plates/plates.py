def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    a = 0
    b = 1
    if len(s) >= 2 and len(s) <= 6:
        if s.isalnum():
            if s[:2].isalpha():
                b = 0
                for i in s:
                    if i.isnumeric() and a == 0 and i == '0':
                        b = 1
                    elif i.isnumeric() and i != '0' and a == 0:
                        a += 1
                    elif i.isnumeric() and a > 0:
                        a += 1
                    elif i.isalpha() and a > 0:
                        b = 1
    if b == 0:
        return True
        
if __name__ == "__main__":
    main()
