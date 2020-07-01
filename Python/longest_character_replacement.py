"""
Longest Repeating Character Replacement.

Given a string s that consists of only uppercase English letters, you can
perform at most k operations on that string. In one operation, you can choose
any character of the string and change it to any other uppercase English
character. Find the length of the longest sub-string containing all repeating
letters you can get after performing the above operations.

EXAMPLE:
s = "ABAB", k = 2 -> 4

s = "AABABBA", k = 1 -> 4
"""

print()

# METHOD 1a - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1a')


def character_replacement(s, k):
    """
    Find the longest repeating substring with k replacements.

    LOGIC:
    Using the sliding window technique, the condition will be number of extra
    characters (this uses a helper function to get the most common letter)

    INPUT:
    s: a string
    k: an integer representing the number of replacements

    OUTPUT:
    The length of the longest substring with repeating characters
    """
    size = len(s)
    max_length = 0

    if not size:
        return max_length

    if size <= k:
        return size

    from collections import defaultdict
    letters = defaultdict(int)
    left = 0
    right = 0

    def get_letter_count():
        max_counter = 0

        for letter in letters:
            if letters[letter] > max_counter:
                max_counter = letters[letter]

        return max_counter

    while right < size:
        letters[s[right]] += 1
        right += 1

        max_counter = get_letter_count()

        while right - left > max_counter + k:
            letters[s[left]] -= 1
            left += 1

            max_counter = get_letter_count()

        max_length = max(max_length, right - left)

    return max_length


# TEST CASES
TEST_A = "ABAB"

TEST_AA = 2
TEST_AB = 0

RESULT_AA = character_replacement(TEST_A, TEST_AA)
RESULT_AB = character_replacement(TEST_A, TEST_AB)

CORRECT_AA = 4
CORRECT_AB = 1

TEST_B = "AABABBA"

TEST_BA = 1
TEST_BB = 2

RESULT_BA = character_replacement(TEST_B, TEST_BA)
RESULT_BB = character_replacement(TEST_B, TEST_BB)

CORRECT_BA = 4
CORRECT_BB = 5

TEST_C = "ABCDA"

TEST_CA = 1
TEST_CB = 3

RESULT_CA = character_replacement(TEST_C, TEST_CA)
RESULT_CB = character_replacement(TEST_C, TEST_CB)

CORRECT_CA = 2
CORRECT_CB = 5

print("Testing AA: ", end="")
print("OK" if RESULT_AA == CORRECT_AA
      else "FAIL (" + str(RESULT_AA) + " vs " + str(CORRECT_AA) + ")")

print("Testing AB: ", end="")
print("OK" if RESULT_AB == CORRECT_AB
      else "FAIL (" + str(RESULT_AB) + " vs " + str(CORRECT_AB) + ")")

print("Testing BA: ", end="")
print("OK" if RESULT_BA == CORRECT_BA
      else "FAIL (" + str(RESULT_BA) + " vs " + str(CORRECT_AA) + ")")

print("Testing BB: ", end="")
print("OK" if RESULT_BB == CORRECT_BB
      else "FAIL (" + str(RESULT_BB) + " vs " + str(CORRECT_BB) + ")")

print("Testing CA: ", end="")
print("OK" if RESULT_CA == CORRECT_CA
      else "FAIL (" + str(RESULT_CA) + " vs " + str(CORRECT_CA) + ")")

print("Testing CB: ", end="")
print("OK" if RESULT_CB == CORRECT_CB
      else "FAIL (" + str(RESULT_CB) + " vs " + str(CORRECT_CB) + ")")

print()

# METHOD 1b - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1b')


def character_replacement(s, k):
    """
    Find the longest repeating substring with k replacements.

    LOGIC:
    Using the sliding window technique, the condition will be number of extra
    characters (this uses a max value for the most common letter)

    INPUT:
    s: a string
    k: an integer representing the number of replacements

    OUTPUT:
    The length of the longest substring with repeating characters
    """
    size = len(s)
    max_length = 0

    if not size:
        return max_length

    if size <= k:
        return size

    from collections import defaultdict
    letters = defaultdict(int)
    left = 0
    right = 0
    most_common_counter = 0

    while right < size:
        letters[s[right]] += 1
        most_common_counter = max(most_common_counter, letters[s[right]])
        right += 1

        if right - left > most_common_counter + k:
            letters[s[left]] -= 1
            left += 1

        max_length = max(max_length, right - left)

    return max_length


# TEST CASES
TEST_A = "ABAB"

TEST_AA = 2
TEST_AB = 0

RESULT_AA = character_replacement(TEST_A, TEST_AA)
RESULT_AB = character_replacement(TEST_A, TEST_AB)

CORRECT_AA = 4
CORRECT_AB = 1

TEST_B = "AABABBA"

TEST_BA = 1
TEST_BB = 2

RESULT_BA = character_replacement(TEST_B, TEST_BA)
RESULT_BB = character_replacement(TEST_B, TEST_BB)

CORRECT_BA = 4
CORRECT_BB = 5

TEST_C = "ABCDA"

TEST_CA = 1
TEST_CB = 3

RESULT_CA = character_replacement(TEST_C, TEST_CA)
RESULT_CB = character_replacement(TEST_C, TEST_CB)

CORRECT_CA = 2
CORRECT_CB = 5

print("Testing AA: ", end="")
print("OK" if RESULT_AA == CORRECT_AA
      else "FAIL (" + str(RESULT_AA) + " vs " + str(CORRECT_AA) + ")")

print("Testing AB: ", end="")
print("OK" if RESULT_AB == CORRECT_AB
      else "FAIL (" + str(RESULT_AB) + " vs " + str(CORRECT_AB) + ")")

print("Testing BA: ", end="")
print("OK" if RESULT_BA == CORRECT_BA
      else "FAIL (" + str(RESULT_BA) + " vs " + str(CORRECT_AA) + ")")

print("Testing BB: ", end="")
print("OK" if RESULT_BB == CORRECT_BB
      else "FAIL (" + str(RESULT_BB) + " vs " + str(CORRECT_BB) + ")")

print("Testing CA: ", end="")
print("OK" if RESULT_CA == CORRECT_CA
      else "FAIL (" + str(RESULT_CA) + " vs " + str(CORRECT_CA) + ")")

print("Testing CB: ", end="")
print("OK" if RESULT_CB == CORRECT_CB
      else "FAIL (" + str(RESULT_CB) + " vs " + str(CORRECT_CB) + ")")

print()
