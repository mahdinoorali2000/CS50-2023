# TODO
import cs50

h = cs50.get_int("Height: ")
while h < 1 or h > 8:
    h = int(input("Height: "))

for i in range(h):
    print((h - i - 1) * " " + (i + 1) * "#" + "  ", end="")
    print((i + 1) * "#")
