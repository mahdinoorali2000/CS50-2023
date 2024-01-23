def main():
    txt = input("Input: ")
    print(f"{rm_vowels(txt)}")

def rm_vowels(st):
    v = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    result = ""
    for c in st:
        if c not in v:
            result += c
    return result

main()
