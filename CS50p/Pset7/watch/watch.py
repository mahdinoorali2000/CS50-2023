import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        link = re.search('(?<=embed).*?(?=")', s)
        return "https://youtu.be" + link.group(0)
    except:
        return None

if __name__ == "__main__":
    main()
