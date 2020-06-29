"""
Max Sum Subarray.

Given an integer array nums, find the contiguous subarray within an array
(containing at least one number) which has the largest sum.

EXAMPLE:
nums = [2,3,-2,4] -> 5
"""

print()

# METHOD 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1')


def max_sum(nums):
    """
    Max sum of a contiguous subarray in nums.

    LOGIC:
    Brute force approach by going through all the possible sublists in nums and
    calculating the sum

    INPUT:
    nums: a list of integers

    OUTPUT:
    The max sum of a contiguous subarray in nums
    """
    size = len(nums)

    if not size:
        return None

    if size == 1:
        return nums[0]

    result = float('-inf')

    for i in range(size):
        for j in range(i+1, size+1):
            local_sum = max(nums[i], sum(nums[i:j]))
            result = max(result, local_sum)

    return max_sum


# TEST CASES
TEST_A = [2, 3, -2, 4]
TEST_B = [-2, 0, -1]
TEST_C = [-7, 8, 3, 0, 12, -1]
TEST_D = [1]
TEST_E = [-2, 4, 3]
TEST_F = [0, 2, 2]
TEST_G = [-2, 3, -4]
TEST_H = [2, -5, 0, 4, 3, 0]
TEST_I = [-3, 0, 1, -2]

RESULT_A = max_sum(TEST_A)
RESULT_B = max_sum(TEST_B)
RESULT_C = max_sum(TEST_C)
RESULT_D = max_sum(TEST_D)
RESULT_E = max_sum(TEST_E)
RESULT_F = max_sum(TEST_F)
RESULT_G = max_sum(TEST_G)
RESULT_H = max_sum(TEST_H)
RESULT_I = max_sum(TEST_I)

CORRECT_A = 7
CORRECT_B = 0
CORRECT_C = 23
CORRECT_D = 1
CORRECT_E = 7
CORRECT_F = 4
CORRECT_G = 3
CORRECT_H = 7
CORRECT_I = 1

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

print("Testing G: ", end="")
print("OK" if RESULT_G == CORRECT_G
      else "FAIL (" + str(RESULT_G) + " vs " + str(CORRECT_G) + ")")

print("Testing H: ", end="")
print("OK" if RESULT_H == CORRECT_H
      else "FAIL (" + str(RESULT_H) + " vs " + str(CORRECT_H) + ")")

print("Testing I: ", end="")
print("OK" if RESULT_I == CORRECT_I
      else "FAIL (" + str(RESULT_I) + " vs " + str(CORRECT_I) + ")")

print()

# METHOD 2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 2')


def max_sum(nums):
    """
    Max sum of a contiguous subarray in nums.

    LOGIC:
    Using Kadane's algorithm (local_max = max(nums[i],
    nums[i] + local_max in nums[i-1]))

    INPUT:
    nums: a list of integers

    OUTPUT:
    The max sum of a contiguous subarray in nums
    """
    size = len(nums)

    if not size:
        return None

    if size == 1:
        return nums[0]

    result = float('-inf')
    local_max = nums[0]

    for i in range(1, size):
        local_max = max(nums[i], nums[i] + local_max)
        result = max(result, local_max)

    return result


# TEST CASES
RESULT_A = max_sum(TEST_A)
RESULT_B = max_sum(TEST_B)
RESULT_C = max_sum(TEST_C)
RESULT_D = max_sum(TEST_D)
RESULT_E = max_sum(TEST_E)
RESULT_F = max_sum(TEST_F)
RESULT_G = max_sum(TEST_G)
RESULT_H = max_sum(TEST_H)
RESULT_I = max_sum(TEST_I)


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

print("Testing G: ", end="")
print("OK" if RESULT_G == CORRECT_G
      else "FAIL (" + str(RESULT_G) + " vs " + str(CORRECT_G) + ")")

print("Testing H: ", end="")
print("OK" if RESULT_H == CORRECT_H
      else "FAIL (" + str(RESULT_H) + " vs " + str(CORRECT_H) + ")")

print("Testing I: ", end="")
print("OK" if RESULT_I == CORRECT_I
      else "FAIL (" + str(RESULT_I) + " vs " + str(CORRECT_I) + ")")

print()
