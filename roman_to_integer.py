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