while True:
    x, y, z = input("Expression: ").split(" ")
    if not (y == "/" and z == "0"):
        break

match y:
    case "-":
        print("{:.1f}".format(float(x) - float(z)))
    case "+":
        print("{:.1f}".format(float(x) + float(z)))
    case "*":
        print("{:.1f}".format(float(x) * float(z)))
    case "/":
        print("{:.1f}".format(float(x) / float(z)))
