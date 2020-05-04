
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