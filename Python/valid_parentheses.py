# DESCRIPTION:
# Given a string with different parentheses characters, determine if it is
# valid.

# EXAMPLE:
# "()[]{}" -> True

# INPUT:
# A string with a set of parentheses

# OUTPUT:
# A boolean that states if it is a valid pattern of parentheses

input_str = "(([]){})"
print()

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC:
# This method uses a stack to keep track of the opening character and match the
# last in the stack with a closing character

def valid(input_str):
    stack = []
    pairs = {'}': '{', ']': '[', ')': '('}

    for i in input_str:
        if i in pairs.values():
            stack.append(i)
        if i in pairs.keys():
            if len(stack) == 0 or stack.pop() != pairs[i]:
                return False

    if len(stack) != 0:
        return False

    return True

print(valid(input_str))
print()
