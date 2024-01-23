import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)
    else:
        print (counter(sys.argv[1]))

def counter(pfile):
    with open(pfile) as file:
        lines = file.readlines()
    n = 0
    for l in lines:
        if l.strip().startswith("#") or l.strip().startswith("\n") or l.isspace():
            n += 1

    return len(lines) - n


if __name__ == "__main__":
    main()
