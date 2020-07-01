"""
Reverse String.

Create your own reverse function that reverses the characters in a string
Cannot use string[::-1] or reversed(string)

EXAMPLE:
'Hello World!' -> '!dlroW olleH'
"""

print()


# METHOD 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1')


def reverse_string(s):
    """
    Reverse a string.

    LOGIC:
    Use recursion to traverse the string and concatenating the characters
    backwards

    INPUT:
    A string

    OUTPUT:
    The input string but reversed
    """
    if s == '':
        return s

    return reverse_string(s[1:]) + s[0]


# TEST CASES
TEST_A = "Hello World!"

RESULT_A = reverse_string(TEST_A)

CORRECT_A = "!dlroW olleH"

print("Testing A: ", end="")
print("OK" if RESULT_A == CORRECT_A
      else "FAIL (" + str(RESULT_A) + " vs " + str(CORRECT_A) + ")")

print()


# METHOD 2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 2')


def reverse_string(s):
    """
    Reverse a string.

    LOGIC:
    Using the idea of two pointers and swapping them until they meet in the
    middle. This method uses a list to swap the charaters.

    INPUT:
    A string

    OUTPUT:
    The input string but reversed
    """
    list_str = list(s)
    i = 0
    j = len(list_str) - 1

    while (i < j):
        if list_str[i] != list_str[j]:
            list_str[i], list_str[j] = list_str[j], list_str[i]

        i += 1
        j -= 1

    return ''.join(list_str)


# TEST CASES
TEST_A = "Hello World!"

RESULT_A = reverse_string(TEST_A)

CORRECT_A = "!dlroW olleH"

print("Testing A: ", end="")
print("OK" if RESULT_A == CORRECT_A
      else "FAIL (" + str(RESULT_A) + " vs " + str(CORRECT_A) + ")")

print()

# METHOD 3 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 3')


def reverse_string(s):
    """
    Reverse a string.

    LOGIC:
    Using the idea of two pointers and swapping them until they meet in the
    middle. This method uses string slicing and concatenation to swap
    characters.

    INPUT:
    A string

    OUTPUT:
    The input string but reversed
    """
    i = 0
    j = len(s) - 1
    copy = s

    while i < j:
        prefix = copy[:i]
        middle = copy[i+1:j]
        suffix = copy[j+1:]

        copy = prefix + copy[j] + middle + copy[i] + suffix

        i += 1
        j -= 1

    return copy


# TEST CASES
TEST_A = "Hello World!"

RESULT_A = reverse_string(TEST_A)

CORRECT_A = "!dlroW olleH"

print("Testing A: ", end="")
print("OK" if RESULT_A == CORRECT_A
      else "FAIL (" + str(RESULT_A) + " vs " + str(CORRECT_A) + ")")

print()
