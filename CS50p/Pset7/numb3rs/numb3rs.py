import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        ip = ip.split(".")
        if len(ip) != 4:
            return False
        for i in ip:
            if int(i) > 255:
                return False
    except ValueError:
        return False
    else:
        return True



if __name__ == "__main__":
    main()
