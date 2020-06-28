# DESCRIPTION:
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest product.

# EXAMPLE:
# nums = [2,3,-2,4] -> 6

# INPUT:
# A list of integers

# OUTPUT:
# The max product of a contiguous subarray in nums

print()

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC:
# Brute force approach by going through all the possible sublists in nums and
# calculating the product

def maxProduct(nums):
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



A = [2,3,-2,4]
B = [-2,0,-1]
C = [-7,8,3,0,12,-1]
D = [1]
E = [-2,4,3]
F = [0,2,2]
G = [-2,3,-4]
H = [2,-5,-2,-4,3]
I = [-3,0,1,-2]

RESULT_A = maxProduct(A)
RESULT_B = maxProduct(B)
RESULT_C = maxProduct(C)
RESULT_D = maxProduct(D)
RESULT_E = maxProduct(E)
RESULT_F = maxProduct(F)
RESULT_G = maxProduct(G)
RESULT_H = maxProduct(H)
RESULT_I = maxProduct(I)

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
print("OK" if RESULT_A == CORRECT_A else "FAIL (" + str(RESULT_A) + " vs " + str(CORRECT_A) + ")")

print("Testing B: ", end="")
print("OK" if RESULT_B == CORRECT_B else "FAIL (" + str(RESULT_B) + " vs " + str(CORRECT_B) + ")")

print("Testing C: ", end="")
print("OK" if RESULT_C == CORRECT_C else "FAIL (" + str(RESULT_C) + " vs " + str(CORRECT_C) + ")")

print("Testing D: ", end="")
print("OK" if RESULT_D == CORRECT_D else "FAIL (" + str(RESULT_D) + " vs " + str(CORRECT_D) + ")")

print("Testing E: ", end="")
print("OK" if RESULT_E == CORRECT_E else "FAIL (" + str(RESULT_E) + " vs " + str(CORRECT_E) + ")")

print("Testing F: ", end="")
print("OK" if RESULT_F == CORRECT_F else "FAIL (" + str(RESULT_F) + " vs " + str(CORRECT_F)+ ")")

print("Testing G: ", end="")
print("OK" if RESULT_G == CORRECT_G else "FAIL (" + str(RESULT_G) + " vs " + str(CORRECT_G) + ")")

print("Testing H: ", end="")
print("OK" if RESULT_H == CORRECT_H else "FAIL (" + str(RESULT_H) + " vs " + str(CORRECT_H) + ")")

print("Testing I: ", end="")
print("OK" if RESULT_I == CORRECT_I else "FAIL (" + str(RESULT_I) + " vs " + str(CORRECT_I) + ")")

print()

# METHOD 2 - - - - -
print('METHOD 2')

# LOGIC:
# Using Kadane's algorithm, we keep track of min because of negatives (- * - may be greater than the
# current value)

def maxProduct(nums):
    size = len(nums)

    if size == 1:
        return nums[0]

    max_product = nums[0]
    current_max_product = nums[0]
    current_min_product = nums[0]

    for i in range(1, size):
        num = nums[i]

        prev_min_product = current_max_product
        prev_max_product = current_min_product

        current_min_product = min(prev_min_product * num, prev_max_product * num, num)
        current_max_product = max(prev_min_product * num, prev_max_product * num, num)

        max_product = max(max_product, current_max_product)

    return max_product

RESULT_A = maxProduct(A)
RESULT_B = maxProduct(B)
RESULT_C = maxProduct(C)
RESULT_D = maxProduct(D)
RESULT_E = maxProduct(E)
RESULT_F = maxProduct(F)
RESULT_G = maxProduct(G)
RESULT_H = maxProduct(H)
RESULT_I = maxProduct(I)

print("Testing A: ", end="")
print("OK" if RESULT_A == CORRECT_A else "FAIL (" + str(RESULT_A) + " vs " + str(CORRECT_A) + ")")

print("Testing B: ", end="")
print("OK" if RESULT_B == CORRECT_B else "FAIL (" + str(RESULT_B) + " vs " + str(CORRECT_B) + ")")

print("Testing C: ", end="")
print("OK" if RESULT_C == CORRECT_C else "FAIL (" + str(RESULT_C) + " vs " + str(CORRECT_C) + ")")

print("Testing D: ", end="")
print("OK" if RESULT_D == CORRECT_D else "FAIL (" + str(RESULT_D) + " vs " + str(CORRECT_D) + ")")

print("Testing E: ", end="")
print("OK" if RESULT_E == CORRECT_E else "FAIL (" + str(RESULT_E) + " vs " + str(CORRECT_E) + ")")

print("Testing F: ", end="")
print("OK" if RESULT_F == CORRECT_F else "FAIL (" + str(RESULT_F) + " vs " + str(CORRECT_F)+ ")")

print("Testing G: ", end="")
print("OK" if RESULT_G == CORRECT_G else "FAIL (" + str(RESULT_G) + " vs " + str(CORRECT_G) + ")")

print("Testing H: ", end="")
print("OK" if RESULT_H == CORRECT_H else "FAIL (" + str(RESULT_H) + " vs " + str(CORRECT_H) + ")")

print("Testing I: ", end="")
print("OK" if RESULT_I == CORRECT_I else "FAIL (" + str(RESULT_I) + " vs " + str(CORRECT_I) + ")")

print()