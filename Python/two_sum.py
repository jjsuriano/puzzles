"""
Two Sum.

Given an array of integers, return indices of the two numbers such that they
add up to a specific target. You may assume that each input would have exactly
one solution, and you may not use the same element twice.

EXAMPLE:
num = [2, 7, 11, 15], target = 9 -> [0, 1]
"""

print()

# METHOD 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1')


def two_sum(nums, target):
    """
    Check if two elements have the sum of target.

    LOGIC:
    Loop through all the numbers and add the difference (target - num) to a
    dictionary as a key and a value of i if the current num in the for loop is
    a key of the dictionary then return the value of dict[num] and i dict[num]
    has the index of the other number (target - num)

    INPUT:
    nums: a list with integers
    target: the target sum we are looking for

    OUTPUT:
    The two indices of the numbers that have the sum of target
    """
    indices = dict()

    for i, num in enumerate(nums):
        if num in indices:
            return (indices[num], i)
        else:
            indices[target - num] = i
    return ()


TEST_A = [2, 7, 11, 15]

TEST_AA = 9
TEST_AB = 10

RESULT_AA = two_sum(TEST_A, TEST_AA)
RESULT_AB = two_sum(TEST_A, TEST_AB)

CORRECT_AA = (0, 1)
CORRECT_AB = ()

print("Testing AA: ", end="")
print("OK" if RESULT_AA == CORRECT_AA
      else "FAIL (" + str(RESULT_AA) + " vs " + str(CORRECT_AA) + ")")

print("Testing AB: ", end="")
print("OK" if RESULT_AB == CORRECT_AB
      else "FAIL (" + str(RESULT_AB) + " vs " + str(CORRECT_AB) + ")")

print()
