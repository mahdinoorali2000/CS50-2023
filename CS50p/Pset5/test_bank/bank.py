def main():
    s = input("Greeting: ").strip()
    print(f"${value(s)}")

def value(greeting):
    if greeting.lower().startswith("hello",0):
        return 0
    elif greeting.lower().startswith("h",0):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
