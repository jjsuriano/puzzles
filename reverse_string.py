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
# This method uses a list to swap the charaters

list_str = list(string)
i = 0
j = len(list_str) - 1
while (i < j):
    if list_str[i] != list_str[j]:
        list_str[i], list_str[j] = list_str[j], list_str[i]
    i += 1
    j -= 1

reversed_str = ''.join(list_str)

print('The reversed version of the string is: \'' + reversed_str + '\'.')
print()

# METHOD 3 - - - - -
print('METHOD 3')
# LOGIC: 
# Using the idea of two pointers and swapping them until they meet in the middle
# This method uses string slicing and concatenation to swap characters

i = 0
j = len(string) - 1
copy = string

while i < j:
    prefix = copy[:i]
    middle = copy[i+1:j]
    suffix = copy[j+1:]
    copy = prefix + copy[j] + middle + copy[i] + suffix
    i += 1
    j -= 1

print('The reversed version of the string is: \'' + copy + '\'.')
print()
