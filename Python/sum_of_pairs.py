"""
Sum of pairs.

Find how many pairs have the sum equal to the variable 'sum' in a given list
of numbers. No duplicates are allowed (a value can be used only one time).

EXAMPLE:
nums = [1, 3, 4, 8, 2, 5], sum = 5 -> 2
"""

print()

# METHOD 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1')


def pairs_with_sum(nums, target):
    """
    Return the number of pairs in nums that sum to target.

    LOGIC:
    A brute force solution that adds up an element with another element to see
    if they match the desired sum.

    INPUT:
    nums: an array of numbers
    target: the desired sum

    OUTPUT:
    The number of pairs that match the sum when added
    """
    pairs = []
    used = []

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            x = nums[i]
            y = nums[j]

            if x+y == target and not(i in used or j in used):
                pairs.append((x, y))
                used.append(i)
                used.append(j)
                break

    return len(pairs)


# TEST CASES
TEST_A = [1, 3, 4, 8, 2, 5]
TEST_AA = 5

RESULT_AA = pairs_with_sum(TEST_A, TEST_AA)

CORRECT_AA = 2

print("Testing A: ", end="")
print("OK" if RESULT_AA == CORRECT_AA
      else "FAIL (" + str(RESULT_AA) + " vs " + str(CORRECT_AA) + ")")

print()

# METHOD 2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 2')


def pairs_with_sum(nums, target):
    """
    Return the number of pairs in nums that sum to target.

    LOGIC:
    This solution finds the number of times a number appears in the input list.
    Using that frequency table, find the matching pairs that add up to 'sum'.

    INPUT:
    nums: an array of numbers
    target: the desired sum

    OUTPUT:
    The number of pairs that match the sum when added
    """
    frequency = {}
    counter = 0

    for i in nums:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] += 1

    for i in frequency:
        find = target - i

        if (i == find and frequency[i] <= 1):
            continue

        if find in frequency and frequency[find] != 0 and frequency[i] != 0:
            appearances = min(frequency[i], frequency[find])

            if find == i:
                appearances //= 2

            counter += appearances
            frequency[find] -= appearances
            frequency[i] -= appearances

    return counter


# TEST CASES
TEST_A = [1, 3, 4, 8, 2, 5]
TEST_AA = 5

RESULT_AA = pairs_with_sum(TEST_A, TEST_AA)

CORRECT_AA = 2

print("Testing A: ", end="")
print("OK" if RESULT_AA == CORRECT_AA
      else "FAIL (" + str(RESULT_AA) + " vs " + str(CORRECT_AA) + ")")

print()
