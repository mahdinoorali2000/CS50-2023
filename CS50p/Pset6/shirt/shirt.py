from PIL import Image, ImageOps
import sys
import os

def main():
    if len(sys.argv) < 3:
        print("Too few command-line arguments   ")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not (echeck(sys.argv[1]) and echeck(sys.argv[2])):
        print("Invalid output")
        sys.exit(1)
    elif not endcheck(sys.argv[1], sys.argv[2]):
        print("Input and output have different extensions")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("Input does not exist")
        sys.exit(1)
    else:
        shr(sys.argv[1] , sys.argv[2])

def echeck(a):
    extensions = ["jpg", "jpeg", "png"]
    _, x = a.split(".")
    if x in extensions:
        return True
    else:
        return False

def endcheck(a, b):
    _, x = a.split(".")
    _, z = b.split(".")
    if x == z:
        return True
    else:
        return False

def shr(a, b):
    shirt = Image.open("shirt.png")
    u_image = Image.open(a)

    x, y = shirt.size
    u_image = ImageOps.fit(u_image, (x, y))

    u_image.paste(shirt,shirt)
    u_image.save(b)


if __name__ == "__main__":
    main()
