"""
Valid Parentheses.

Given a string with different parentheses characters, determine if it is
valid.

EXAMPLE:
"()[]{}" -> True
"""

print()

# METHOD 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1')


def valid_parentheses(s):
    """
    Determine if the input string contains valid pairs of parentheses.

    LOGIC:
    This method uses a stack to keep track of the opening character and match
    the last in the stack with a closing character

    INPUT:
    A string with a set of parentheses

    OUTPUT:
    A boolean that states if it is a valid pattern of parentheses
    """
    if not s:
        return True

    pairs = {'}': '{', ']': '[', ')': '('}

    if s[0] in pairs.keys() or s[-1] in pairs.values():
        return False

    stack = []

    for i in s:
        if i in pairs.values():
            stack.append(i)

        if i in pairs.keys():
            if len(stack) == 0 or stack.pop() != pairs[i]:
                return False

    if len(stack) != 0:
        return False

    return True


# TEST CASES
TEST_A = "(([]){})"
TEST_B = "(){((}}){)()"
TEST_C = "{(([[]()]))}"
TEST_D = "()[]{}"

RESULT_A = valid_parentheses(TEST_A)
RESULT_B = valid_parentheses(TEST_B)
RESULT_C = valid_parentheses(TEST_C)
RESULT_D = valid_parentheses(TEST_D)

CORRECT_A = True
CORRECT_B = False
CORRECT_C = True
CORRECT_D = True

print("Testing A: ", end="")
print("OK" if RESULT_A == CORRECT_A
      else "FAIL (" + str(RESULT_A) + " vs " + str(CORRECT_A) + ")")

print("Testing B: ", end="")
print("OK" if RESULT_B == CORRECT_B
      else "FAIL (" + str(RESULT_B) + " vs " + str(CORRECT_B) + ")")

print("Testing C: ", end="")
print("OK" if RESULT_C == CORRECT_C
      else "FAIL (" + str(RESULT_C) + " vs " + str(CORRECT_C) + ")")

print("Testing D: ", end="")
print("OK" if RESULT_D == CORRECT_D
      else "FAIL (" + str(RESULT_D) + " vs " + str(CORRECT_D) + ")")

print()
