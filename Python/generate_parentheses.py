# DESCRIPTION:
# Given n pairs of parentheses, write a function to generate all combinations of
# well-formed parentheses.

# EXAMPLE:
# 3 -> ["((()))",
#       "(()())",
#       "(())()",
#       "()(())",
#       "()()()"]

# INPUT: 
# An int 

# OUTPUT: 
# A list with all the possible combinations of well-formed parentheses

n = 3
print()

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC: 
# This method uses recursion to find all the possible combinations

def matching_parentheses(opening, closing, current, combinations=None):
    if combinations is None:
        combinations = []

    if opening == 0 and closing == 0:
        combinations.append(current)
        return

    if opening == 0 or closing == 0 or (closing < opening):
        return
    
    opening -= 1
    current += '('
    matching_parentheses(opening, closing, current, combinations)
    while closing > 0:
        closing -= 1
        current += ')'
        matching_parentheses(opening, closing, current, combinations)
    return combinations

print(matching_parentheses(n, n, ''))
print()
