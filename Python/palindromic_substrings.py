"""
Palindromic Substrings.

Given a string, your task is to count how many palindromic substrings in this
string. The substrings with different start indexes or end indexes are counted
as different substrings even they consist of same characters.

EXAMPLE:
"abc" -> 3

"aaa" -> 6
"""

print()

# METHOD 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1')


def num_of_palindromic_substrings(s):
    """
    Calculate the number of palindromic substrings.

    LOGIC:
    Brute force solution iterating through all the substrings

    INPUT:
    s, a string

    OUTPUT:
    An integer indicating the number of palindromic substrings the input string
    has.
    """
    palindromic_substrings = []

    for i in range(len(s)):
        palindromic_substrings.append(s[i])

        for j in range(i+1, len(s)):
            current_s = s[i:j+1]

            if current_s == current_s[::-1]:
                palindromic_substrings.append(current_s)

    return len(palindromic_substrings)


# TEST CASES
TEST_A = "abc"
TEST_B = "aaa"

RESULT_A = num_of_palindromic_substrings(TEST_A)
RESULT_B = num_of_palindromic_substrings(TEST_B)

CORRECT_A = 3
CORRECT_B = 6

print("Testing A: ", end="")
print("OK" if RESULT_A == CORRECT_A
      else "FAIL (" + str(RESULT_A) + " vs " + str(CORRECT_A) + ")")

print("Testing B: ", end="")
print("OK" if RESULT_B == CORRECT_B
      else "FAIL (" + str(RESULT_B) + " vs " + str(CORRECT_B) + ")")

print()

# METHOD 2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 2')


def num_of_palindromic_substrings(s):
    """
    Calculate the number of palindromic substrings.

    LOGIC:


    INPUT:
    s, a string

    OUTPUT:
    An integer indicating the number of palindromic substrings the input string
    has.
    """
    pass  # TODO


# TEST CASES
RESULT_A = num_of_palindromic_substrings(TEST_A)
RESULT_B = num_of_palindromic_substrings(TEST_B)

print("Testing A: ", end="")
print("OK" if RESULT_A == CORRECT_A
      else "FAIL (" + str(RESULT_A) + " vs " + str(CORRECT_A) + ")")

print("Testing B: ", end="")
print("OK" if RESULT_B == CORRECT_B
      else "FAIL (" + str(RESULT_B) + " vs " + str(CORRECT_B) + ")")

print()
