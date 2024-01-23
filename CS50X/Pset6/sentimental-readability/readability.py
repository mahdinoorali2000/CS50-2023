# TODO
from cs50 import get_string

txt = get_string("Text: ")

let = 0
sent = 0

for x in txt:
    if x.isalpha():
        let += 1

word = len(txt.split())

for x in txt:
    if x == "?" or x == "!" or x == ".":
        sent += 1

L = let / (word / 100)
S = sent / (word / 100)

i = round(0.0588 * L - 0.296 * S - 15.8)

if i < 1:
    print("Before Grade 1")
elif i >= 16:
    print("Grade 16+")
else:
    print(f"Grade {i}")
