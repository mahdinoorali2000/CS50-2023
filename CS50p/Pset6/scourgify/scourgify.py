import os
import csv
import sys

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print("not csv file")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print(f"Could not read {sys.argv[1]}")
        sys.exit(1)
    else:
        scour(sys.argv[1], sys.argv[2])

def scour(file1, file2):
    with open(file1) as rcv:
        read = csv.DictReader(rcv, delimiter = ",")

        with open(file2, "w") as wcv:
            write = csv.DictWriter(wcv, fieldnames = ["first", "last", "house"] )
            write.writeheader()

            for i in read:
                last, first = i["name"].split(",")
                write.writerow({"first": first.strip(), "last": last, "house": i["house"]})


if __name__ == "__main__":
    main()
