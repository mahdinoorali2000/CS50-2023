import os
import sys
import csv
from tabulate import tabulate

def main():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print("Not a CSV file")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        table("File does not exist")
        sys.exit(1)
    else:
        table(sys.argv[1])
def table(file):
    with open(file) as csvf:
        read = csv.DictReader(csvf, delimiter=',')
        print(tabulate(read, headers="keys", tablefmt="grid"))
if __name__ == "__main__":
    main()
