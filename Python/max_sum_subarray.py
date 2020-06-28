# DESCRIPTION:
# Given an integer array nums, find the contiguous subarray within an array
# (containing at least one number) which has the largest sum.

# EXAMPLE:
# nums = [2,3,-2,4] -> 5

# INPUT:
# A list of integers

# OUTPUT:
# The max sum of a contiguous subarray in nums

print()

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC:
# Brute force approach by going through all the possible sublists in nums and
# calculating the sum

def maxSum(nums):
    size = len(nums)

    if not size:
        return None

    if size == 1:
        return nums[0]

    max_sum = float('-inf')

    for i in range(size):
        for j in range(i+1, size+1):
            local_sum = max(nums[i], sum(nums[i:j]))
            max_sum = max(max_sum, local_sum)
    return max_sum

A = [2,3,-2,4] #7
B = [-2,0,-1] #0
C = [-7,8,3,0,12,-1] #23
D = [1] #1
E = [-2,4,3] #7
F = [0,2,2] #4
G = [-2,3,-4] #3
H = [2, -5, 0, 4, 3, 0] #7
I = [-3,0,1,-2] #1

print(maxSum(A))
print(maxSum(B))
print(maxSum(C))
print(maxSum(D))
print(maxSum(E))
print(maxSum(F))
print(maxSum(G))
print(maxSum(H))
print(maxSum(I))

print()

# METHOD 2 - - - - -
print('METHOD 2')

# LOGIC:
# Using Kadane's algorithm

def maxSum(nums):
    size = len(nums)

    if not size:
        return None

    if size == 1:
        return nums[0]

    max_sum = float('-inf')
    local_max = nums[0]

    for i in range(1, size):
        local_max = max(nums[i], nums[i] + local_max)
        max_sum = max(max_sum, local_max)

    return max_sum

print(maxSum(A))
print(maxSum(B))
print(maxSum(C))
print(maxSum(D))
print(maxSum(E))
print(maxSum(F))
print(maxSum(G))
print(maxSum(H))
print(maxSum(I))
print()