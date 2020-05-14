# NAME: 
# Roman to integer

# DESCRIPTION: 
# Take a string with a Roman numeral and return the integer that corresponds to
# that Roman numeral.

# EXAMPLE:
# 'III' -> 3
# 'IV' -> 4

# INPUT: 
# A string representing a Roman numeral

# OUTPUT: 
# An integer

roman = 'MCMXCIV'

print()

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC: 
# A brute force solution to determine the integer value of Roman numeral.

num = 0

for i, d in enumerate(roman):
    if i == 0:
        prev_i = None
    else:
        prev_i = roman[i-1]

    if d == 'I':
        num += 1
    elif d == 'V':
        if prev_i == 'I':
            num += 3
        else: 
            num += 5
    elif d == 'X':
        if prev_i == 'I':
            num += 8
        else: 
            num += 10
    elif d == 'L':
        if prev_i == 'X':
            num += 30
        else: 
            num += 50
    elif d == 'C':
        if prev_i == 'X':
            num += 80
        else: 
            num += 100
    elif d == 'D':
        if prev_i == 'C':
            num += 300
        else: 
            num += 500
    elif d == 'M':
    
        if prev_i == 'C':
            num += 800
        else: 
            num += 1000
    
print(num)
print()

# METHOD 2 - - - - -
print('METHOD 2')

# LOGIC: 
# A solution that refers to a dictionary with valid roman numerals and shortens
# the original string

ROMAN_TO_DEC = {
    'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 
    'X': 10, 'XL': 40, 'L':50, 'XC':90, 
    'C':100, 'CD': 400, 'D': 500, 'CM': 900, 
    'M': 1000,
}

dec = 0

while roman != '':
    if roman[:2] in ROMAN_TO_DEC:
        dec += ROMAN_TO_DEC[roman[:2]]
        roman = roman[2:]
    else:
        dec += ROMAN_TO_DEC[roman[:1]]
        roman = roman[1:]

print(dec)