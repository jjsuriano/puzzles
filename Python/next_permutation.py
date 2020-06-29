"""
Next Permutation.

Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest
possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

EXAMPLE:
1,2,3 -> 1,3,2
"""

print()

# METHOD 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1')


def next_permutation(nums):
    """
    Modify the array to the next larger permutation.

    LOGIC:

    INPUT:
    nums: an array of single digit positive integers

    OUTPUT:
    Nothing, the list is changed in place
    """
    size = len(nums)
    swapped = False
    i = size - 2

    while i >= 0 and not swapped:
        current_num = nums[i]

        if current_num < nums[i + 1]:
            max_diff = float('inf')
            next_biggest = size - 1

            for j in range(i, size):
                diff = nums[j] - current_num
                if diff <= max_diff and diff > 0:
                    max_diff = diff
                    next_biggest = j

            nums[i], nums[next_biggest] = nums[next_biggest], nums[i]
            nums[i+1:] = nums[size-1:i:-1]
            swapped = True

        i -= 1

    if not swapped:
        nums.reverse()

    return nums


# TEST CASES
TEST_A = [1, 2, 3]
TEST_B = [1, 1]
TEST_C = [5, 1, 2, 4, 3, 1]
TEST_D = [1, 1, 5]
TEST_E = [3, 2, 1]
TEST_F = [2, 3, 1, 3, 3]

RESULT_A = next_permutation(TEST_A)
RESULT_B = next_permutation(TEST_B)
RESULT_C = next_permutation(TEST_C)
RESULT_D = next_permutation(TEST_D)
RESULT_E = next_permutation(TEST_E)
RESULT_F = next_permutation(TEST_F)

CORRECT_A = [1, 3, 2]
CORRECT_B = [1, 1]
CORRECT_C = [5, 1, 3, 1, 2, 4]
CORRECT_D = [1, 5, 1]
CORRECT_E = [1, 2, 3]
CORRECT_F = [2, 3, 3, 1, 3]

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

print("Testing E: ", end="")
print("OK" if RESULT_E == CORRECT_E
      else "FAIL (" + str(RESULT_E) + " vs " + str(CORRECT_E) + ")")

print("Testing F: ", end="")
print("OK" if RESULT_F == CORRECT_F
      else "FAIL (" + str(RESULT_F) + " vs " + str(CORRECT_F) + ")")

print()
