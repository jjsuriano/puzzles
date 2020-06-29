"""
Generate Parentheses.

Given n pairs of parentheses, write a function to generate all combinations of
well-formed parentheses.

EXAMPLE:
3 -> ["((()))",
      "(()())",
      "(())()",
      "()(())",
      "()()()"]
"""

n = 3
print()

# METHOD 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1')


def matching_parentheses(n):
    """
    Return all the possible matching parentheses patterns with n parentheses.

    LOGIC:
    This method uses recursion to find all the possible combinations

    INPUT:
    An int

    OUTPUT:
    A list with all the possible combinations of well-formed parentheses
    """
    return _matching_parentheses(n, n, "")


def _matching_parentheses(opening, closing, current, combinations=None):
    """
    Recursion helper function.

    INPUT:
    opening: the number of opening parentheses left
    closing: the number of closing parentheses left
    current: a string with the current combination
    combinations: the list with all the well-formed combinations

    OUTPUT:
    A list with the current combinations of well-formed parentheses
    """
    if combinations is None:
        combinations = []

    if opening == 0 and closing == 0:
        combinations.append(current)
        return combinations

    if opening == 0 or closing == 0 or (closing < opening):
        return combinations

    opening -= 1
    current += '('
    _matching_parentheses(opening, closing, current, combinations)
    while closing > 0:
        closing -= 1
        current += ')'
        _matching_parentheses(opening, closing, current, combinations)
    return combinations


# TEST CASES
TEST_A = 3

RESULT_A = matching_parentheses(TEST_A)

CORRECT_A = [
    "((()))",
    "(()())",
    "(())()",
    "()(())",
    "()()()"
]

print("Testing A: ", end="")
print("OK" if RESULT_A == CORRECT_A
      else "FAIL (" + str(RESULT_A) + " vs " + str(CORRECT_A) + ")")

print()
