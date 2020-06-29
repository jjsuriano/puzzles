"""
Max Product Subarray.

Given an integer array nums, find the largest product of a subarray whithin an
array that contains at least one number

EXAMPLE:
nums = [2,3,-2,4] -> 6
"""

print()

# METHOD 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1')


def max_product(nums):
    """
    Calculate the maximum product of a contiguous subarray in nums.

    LOGIC:
    Brute force approach by going through all the possible sublists in nums and
    calculating the product

    INPUT:
    A list of integers

    OUTPUT:
    The max product of a contiguous subarray in nums
    """
    size = len(nums)

    if size == 1:
        return nums[0]

    max_product = float('-inf')

    for i in range(size):
        if nums[i]:
            current = nums[i]
            max_product = max(max_product, current)
            for j in range(i + 1, size):
                current *= nums[j]
                max_product = max(max_product, current)
        else:
            current = 0
        max_product = max(max_product, current)
    return max_product


# TEST CASES
TEST_A = [2, 3, -2, 4]
TEST_B = [-2, 0, -1]
TEST_C = [-7, 8, 3, 0, 12, -1]
TEST_D = [1]
TEST_E = [-2, 4, 3]
TEST_F = [0, 2, 2]
TEST_G = [-2, 3, -4]
TEST_H = [2, -5, -2, -4, 3]
TEST_I = [-3, 0, 1, -2]

RESULT_A = max_product(TEST_A)
RESULT_B = max_product(TEST_B)
RESULT_C = max_product(TEST_C)
RESULT_D = max_product(TEST_D)
RESULT_E = max_product(TEST_E)
RESULT_F = max_product(TEST_F)
RESULT_G = max_product(TEST_G)
RESULT_H = max_product(TEST_H)
RESULT_I = max_product(TEST_I)

CORRECT_A = 6
CORRECT_B = 0
CORRECT_C = 24
CORRECT_D = 1
CORRECT_E = 12
CORRECT_F = 4
CORRECT_G = 24
CORRECT_H = 24
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


def max_product(nums):
    """
    Calculate the maximum product of a contiguous subarray in nums.

    LOGIC:
    Using Kadane's algorithm, we keep track of min because of negatives (- * -
    may be greater than the current value)

    INPUT:
    A list of integers

    OUTPUT:
    The max product of a contiguous subarray in nums
    """
    size = len(nums)

    if size == 1:
        return nums[0]

    max_product = nums[0]
    current_max_product = nums[0]
    current_min_product = nums[0]

    for i in range(1, size):
        num = nums[i]

        prev_min_product = current_min_product * num
        prev_max_product = current_max_product * num

        current_min_product = min(prev_min_product, prev_max_product, num)
        current_max_product = max(prev_min_product, prev_max_product, num)

        max_product = max(max_product, current_max_product)

    return max_product


# TEST CASES
RESULT_A = max_product(TEST_A)
RESULT_B = max_product(TEST_B)
RESULT_C = max_product(TEST_C)
RESULT_D = max_product(TEST_D)
RESULT_E = max_product(TEST_E)
RESULT_F = max_product(TEST_F)
RESULT_G = max_product(TEST_G)
RESULT_H = max_product(TEST_H)
RESULT_I = max_product(TEST_I)

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
