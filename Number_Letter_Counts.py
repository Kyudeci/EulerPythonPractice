# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

from time import time

start = time()

number_to_text = {
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty",
    30: "thirty",
    40: "forty",
    50: "fifty",
    60: "sixty",
    70: "seventy",
    80: "eighty",
    90: "ninety",
    100: "onehundred",
    200: "twohundred",
    300: "threehundred",
    400: "fourhundred",
    500: "fivehundred",
    600: "sixhundred",
    700: "sevenhundred",
    800: "eighthundred",
    900: "ninehundred",
    1000: "onethousand"
}

collection = ''
for i in range(1,1001):
    if i in number_to_text:
        collection += number_to_text[i]
        continue
    num_text = ''
    stringy = str(i)
    stringy_len = len(stringy)
    for n in range(stringy_len - 1, -1, -1):
        if n == stringy_len - 1 and stringy[n] != '0' and stringy[n-1] != '1':
            num_text += number_to_text[int(stringy[n])]
        if n == stringy_len - 2 and (stringy[n] != '0' and stringy[n] != '1'):
            num_text += number_to_text[int(stringy[n] + '0')]
        elif n == stringy_len - 2 and stringy[n] == '1':
            num_text += number_to_text[int(stringy[n:n+2])]
        if n == stringy_len - 3 and stringy[n] != '0':
            num_text += (number_to_text[int(stringy[n] + '00')] + 'and')
        if n == stringy_len - 4 and stringy[n] != '0':
            num_text += (number_to_text[int(stringy[n] + '000')])
    collection += num_text

print(f"{len(collection)} letters. found in {time()-start} seconds.")
