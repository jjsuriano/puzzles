"""
Longest Ones.

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.
Return the length of the longest (contiguous) subarray that contains only 1s.

EXAMPLE:
A = [1,1,1,0,0,0,1,1,1,1,0], K = 2-> 6
"""

print()

# METHOD 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1')


def longest_ones(nums, K):
    """
    Calculate the longest strings of 1s with K operations.

    LOGIC:
    Using a sliding window approach, expand (by increasing right) until the
    number of zeroes is greater than K, if the number of zeroes is greater than
    K contract the window until the number of zeroes is less or equal to K

    INPUT:
    A list of 1s and 0s, K elements that can be changed

    OUTPUT:
    The length of the longest array with only 1s
    """
    size = len(nums)
    if not size:
        return 0
    if size <= K:
        return size

    result = 0
    left = 0
    right = 0
    counter = 0

    while right < size:
        if not nums[right]:
            counter += 1
        right += 1

        while counter > K:
            if not nums[left]:
                counter -= 1
            left += 1

        result = max(result, right - left)
    return result


# TEST CASES
TEST_A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
TEST_B = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
TEST_C = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]

RESULT_A = longest_ones(TEST_A, 2)
RESULT_B = longest_ones(TEST_B, 0)
RESULT_C = longest_ones(TEST_C, 3)

CORRECT_A = 6
CORRECT_B = 4
CORRECT_C = 10

print("Testing A: ", end="")
print("OK" if RESULT_A == CORRECT_A
      else "FAIL (" + str(RESULT_A) + " vs " + str(CORRECT_A) + ")")

print("Testing B: ", end="")
print("OK" if RESULT_B == CORRECT_B
      else "FAIL (" + str(RESULT_B) + " vs " + str(CORRECT_B) + ")")

print("Testing C: ", end="")
print("OK" if RESULT_C == CORRECT_C
      else "FAIL (" + str(RESULT_C) + " vs " + str(CORRECT_C) + ")")

print()
