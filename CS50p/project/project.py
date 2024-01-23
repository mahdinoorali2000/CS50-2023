from persiantools.jdatetime import JalaliDate, JalaliDateTime
import datetime

def days_until_today(year, month, day):
    try:
        date = f"{year}/{month}/{day}"
        date = datetime.datetime.strptime(date, "%Y/%m/%d")
        now = datetime.datetime.now()
        days_until_today = (now - date).days
        return days_until_today
    except:
        return "False"

# jalali to Gregorian
def convert_jalali(year, month, day):
    try:
        mlist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        klist = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        x = 0
        z = -1
        if(month <= 7):
            days = (month - 1)*31 + day
        else:
            days = (month - 7)*30 + (6 * 31) + day

        g, m = str((year + 2346) * (0.24219858156)).split(".")
        if int(m) < 24219858156:
            kabise = True
        else:
            kabise = False

        if(days < 288 and days > 12 and kabise):
            year += 621
            days -= 12
            for i,y in enumerate(mlist[3:]):
                if(days > y):
                    days -= y
                    x = i + 1
            if(x == 1):
                x -= 1
            month = 4 + x
            day = days

        elif(days < 287 and days > 11 and not kabise):
            year += 621
            days -= 11
            for i,y in enumerate(mlist[3:]):
                if(days > y):
                    days -= y
                    x = i + 1
            if(x == 1):
                x -= 1
            month = 4 + x
            day = days

        elif(days >= 288 and kabise):
            year += 622
            days -= 287
            for i,y in enumerate(mlist[:2]):
                if(days > y):
                    days -= y
                    z = i

            month = 2 + z
            day = days

        elif(days >= 287 and not kabise):
            year += 622
            if(year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
                days -= 286
                for i,y in enumerate(klist[:2]):
                    if(days > y):
                        days -= y
                        z = i

                month = 2 + z
                day = days
            else:
                days -= 286
                for i,y in enumerate(mlist[:2]):
                    if(days > y):
                        days -= y
                        z = i
                month = 2 + z
                day = days

        elif(days <= 12 and kabise):
            year += 621
            month = 3
            day = days + 19

        elif(days <= 11 and not kabise):
            year += 621
            month = 3
            day = days + 20

        return f"{year}/{month}/{day}"
    except:
        return "False"

def convert_Gregorian(year,month,day):
    try:
        year , month , day = str(JalaliDate.to_jalali(year, month, day)).split("-")
        return f"{year}/{month}/{day}"
    except:
        return "False"

def main():
    convert_Gregorian()
    convert_jalali()
    days_until_today()

if __name__ == "__main__":
    main()
