# TODO
from cs50 import get_int

num = get_int("Number: ")
s_list = [int(digit) for digit in str(num)]
num_list = list(reversed([int(digit) for digit in str(num)]))

O = 0
E = 0
for i, digit in enumerate(num_list):
    if (i % 2) == 1:
        do = digit * 2
        if do > 9:
            O += do // 10 + do % 10
        else:
            O += do
    else:
        E += digit
a = s_list[0]*10 + s_list[1]

if (O + E) % 10 == 0:
    if a in [34, 37] and len(num_list) == 15:
        print("AMEX")
    elif a in range(51, 56) and len(num_list) ==16:
        print("MASTERCARD")
    elif s_list[0] == 4 and len(num_list) in [13, 16]:
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")