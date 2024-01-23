from datetime import date
import sys
import inflect

a = inflect.engine()

def main():
    dat = input("Date of Birth: ")
    today = date.today()
    correct = correcting(dat)
    time1 = minut(correct, today)
    print(time(time1))

def correcting(dat):
    try:
        x = date.fromisoformat(dat)
        return x
    except ValueError:
        sys.exit("Invalid date")

def minut(dat, today):
    minus = today - dat
    minutes = minus.days * 24 * 60
    return minutes

def time(time):
    return a.number_to_words(time, andword = "").capitalize() + " minutes"


if __name__ == "__main__":
    main()
