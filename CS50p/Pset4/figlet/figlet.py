import sys
from random import choice
from pyfiglet import Figlet

f = Figlet()
flist = f.getFonts()

if len(sys.argv) == 1:
    txt = input("Input: ")
    f.setFont(font = choice (flist))
    print(f.renderText(txt))
elif len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"] and sys.argv[2] in flist:
        txt = input("Input: ")
        f.setFont(font = sys.argv[2])
        print(f.renderText(txt))
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")
