# DESCRIPTION:
# Create your own reverse function that reverses the characters in a string
# Cannot use string[::-1] or reversed(string)

# EXAMPLE:
# 'Hello World!' -> '!dlroW olleH'

# INPUT: 
# A string

# OUTPUT: 
# The input string but reversed

string = 'Hello World!'
print()
print('The original string is: \'' + string + '\'.')
print()

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC: 
# Use recursion to traverse the string and concatenating the characters 
# backwards

def reverse_string(s):
    if s == '': return s
    return reverse_string(s[1:]) + s[0]

print('The reversed version of the string is: \'' + reverse_string(string) + '\'.')
print()

# METHOD 2 - - - - -
print('METHOD 2')
# LOGIC: 
# Using the idea of two pointers and swapping them until they meet in the middle
reversed_str = list(string)
i = 0
j = len(reversed_str)-1
while (i < j):
    reversed_str[i], reversed_str[j] = reversed_str[j], reversed_str[i]
    i += 1
    j -= 1

reversed_str = ''.join(reversed_str)

print('The reversed version of the string is: \'' + reversed_str + '\'.')
print()