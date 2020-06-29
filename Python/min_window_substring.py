"""
Minimum Window Substring.

Given a string S and a string T, find the minimum window in S which will
contain all the characters in T.

EXAMPLE:
s = "ADOBECODEBANCM", t = "ABC" -> ("BANC", 4)
"""

print()

# METHOD 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1')


def min_window_substring(s, t):
    """
    Calculate the length of the min array in S containing all characters of T.

    LOGIC:
    Use brute force by checking all the substrings in S

    INPUT:
    s: a string
    t: a string

    OUTPUT:
    The minimum window in S that contains all the characters in T and the
    length of the minimum window
    """
    size_s = len(s)
    size_t = len(t)

    if size_s < size_t:
        return ("", 0)

    window = ""
    result = ""

    def checker():
        if len(window) < size_t:
            return False
        for i in t:
            if i not in window:
                return False
        return True

    for i in range(size_s + 1):
        for j in range(i + 1, size_s + 1):
            window = s[i:j]
            if checker():
                if not result or len(result) > j-i:
                    result = window

    return (result, len(result))


# TEST CASES
TEST_A = "ADOBECODEBANCM"

TEST_AA = "ABC"
TEST_AB = "SD"
TEST_AC = "ONE"

RESULT_AA = min_window_substring(TEST_A, TEST_AA)
RESULT_AB = min_window_substring(TEST_A, TEST_AB)
RESULT_AC = min_window_substring(TEST_A, TEST_AC)

CORRECT_AA = ("BANC", 4)
CORRECT_AB = ("", 0)
CORRECT_AC = ("ODEBAN", 6)

print("Testing AA: ", end="")
print("OK" if RESULT_AA == CORRECT_AA
      else "FAIL (" + str(RESULT_AA) + " vs " + str(CORRECT_AA) + ")")

print("Testing AB: ", end="")
print("OK" if RESULT_AB == CORRECT_AB
      else "FAIL (" + str(RESULT_AB) + " vs " + str(CORRECT_AB) + ")")

print("Testing AC: ", end="")
print("OK" if RESULT_AC == CORRECT_AC
      else "FAIL (" + str(RESULT_AC) + " vs " + str(CORRECT_AC) + ")")

TEST_B = "AA"

TEST_BA = "AA"

RESULT_BA = min_window_substring(TEST_B, TEST_BA)

CORRECT_BA = ("AA", 2)
print("Testing BA: ", end="")
print("OK" if RESULT_BA == CORRECT_BA
      else "FAIL (" + str(RESULT_BA) + " vs " + str(CORRECT_BA) + ")")

print()

# METHOD 2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 2')


def min_window_substring(s, t):
    """
    Calculate the length of the min array in S containing all characters of T.

    LOGIC:
    Use the sliding window technique to traverse S only once (dynamic window)

    INPUT:
    s: a string
    t: a string

    OUTPUT:
    The minimum window in S that contains all the characters in T and the
    length of the minimum window
    """
    size_s = len(s)
    size_t = len(t)

    if size_s < size_t:
        return ("", 0)

    from collections import defaultdict, Counter

    left, right = 0, 0
    char_set = Counter(t)
    window = defaultdict(int)
    result = ""

    def checker():
        for i, v in char_set.items():
            if window[i] < v:
                return False
        return True

    while right < size_s:
        current_char = s[right]
        window[current_char] += 1
        right += 1
        while checker():
            if not result or len(result) > right-left:
                result = s[left:right]
            window[s[left]] -= 1
            left += 1

    return (result, len(result))


# TEST CASES
TEST_A = "ADOBECODEBANCM"

TEST_AA = "ABC"
TEST_AB = "SD"
TEST_AC = "ONE"

RESULT_AA = min_window_substring(TEST_A, TEST_AA)
RESULT_AB = min_window_substring(TEST_A, TEST_AB)
RESULT_AC = min_window_substring(TEST_A, TEST_AC)

CORRECT_AA = ("BANC", 4)
CORRECT_AB = ("", 0)
CORRECT_AC = ("ODEBAN", 6)

print("Testing AA: ", end="")
print("OK" if RESULT_AA == CORRECT_AA
      else "FAIL (" + str(RESULT_AA) + " vs " + str(CORRECT_AA) + ")")

print("Testing AB: ", end="")
print("OK" if RESULT_AB == CORRECT_AB
      else "FAIL (" + str(RESULT_AB) + " vs " + str(CORRECT_AB) + ")")

print("Testing AC: ", end="")
print("OK" if RESULT_AC == CORRECT_AC
      else "FAIL (" + str(RESULT_AC) + " vs " + str(CORRECT_AC) + ")")

TEST_B = "AA"

TEST_BA = "AA"

RESULT_BA = min_window_substring(TEST_B, TEST_BA)

CORRECT_BA = ("AA", 2)
print("Testing BA: ", end="")
print("OK" if RESULT_BA == CORRECT_BA
      else "FAIL (" + str(RESULT_BA) + " vs " + str(CORRECT_BA) + ")")

print()
