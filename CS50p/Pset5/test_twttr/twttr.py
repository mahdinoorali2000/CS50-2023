def main():
    txt = input("Input: ")
    print(f"{shorten(txt)}")

def shorten(word):
    v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    for c in word:
        if c not in v:
            result += c
    return result

if __name__ == "__main__":
    main()
