"""
Three Sum.

Given an array nums of n integers, are there elements a, b, c in nums such that
a + b + c = 0? Find all unique triplets in the array which gives the sum of
zero.

EXAMPLE:
num = [-1, 0, 1, 2, -1, -4] -> [
                                  [-1, 0, 1],
                                  [-1, -1, 2],
                               ]
"""

print()

# METHOD 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1')


def three_sum(nums):
    """
    Return all the non-repeating subarrays os size 3 that sum to 0.

    LOGIC:
    Loop through the list and using the current num and using the two_sum
    two-pointer technique in the rest of the list (two pointers technique)

    INPUT:
    A list with integers

    OUTPUT:
    A list will all the sets of three elements that have a sum of 0
    """
    size = len(nums)
    if size < 3:
        return []

    results = []
    nums = sorted(nums)

    for i in range(size - 2):
        if not i or nums[i] != nums[i - 1]:
            target = 0 - nums[i]
            left = i + 1
            right = size - 1

            while left < right:
                two_sum = nums[left] + nums[right]

                if two_sum < target:
                    left += 1
                elif two_sum > target:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

    return results


# TEST CASES
TEST_A = [0, 0, 0, 0]
TEST_B = [-1, 0, 1, 2, -1, -4]
TEST_C = [-1, 0, 1, 2, -1, -4, -1, -1, -1, -1]

RESULT_A = three_sum(TEST_A)
RESULT_B = three_sum(TEST_B)
RESULT_C = three_sum(TEST_C)

CORRECT_A = [[0, 0, 0]]
CORRECT_B = [[-1, -1, 2], [-1, 0, 1]]
CORRECT_C = [[-1, -1, 2], [-1, 0, 1]]

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

# METHOD 2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 2')


def three_sum(nums):
    """
    Return all the non-repeating subarrays os size 3 that sum to 0.

    LOGIC:
    Loop through the list and using the current num and using the two_sum
    two-pointer technique in the rest of the list (dictionary) this uses
    MORE memory than METHOD 1.

    Take advantage of sorting as the time complexity is lower than n^2.

    INPUT:
    A list with integers

    OUTPUT:
    A list will all the sets of three elements that have a sum of 0
    """
    size = len(nums)
    results = []

    if size < 3:
        return results

    nums = sorted(nums)

    for i in range(size - 2):
        if not i or nums[i] != nums[i-1]:
            difference = dict()
            target = 0 - nums[i]
            j = i + 1

            while j < size:
                if nums[j] in difference:
                    results.append([nums[i], difference[nums[j]], nums[j]])

                    while j < size and nums[j-1] == nums[j]:
                        j += 1

                else:
                    difference[target - nums[j]] = nums[j]

                j += 1

    return results


# TEST CASES
RESULT_A = three_sum(TEST_A)
RESULT_B = three_sum(TEST_B)
RESULT_C = three_sum(TEST_C)

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
