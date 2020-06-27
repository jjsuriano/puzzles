# DESCRIPTION:
# Given an array nums of n integers, are there elements a, b, c in nums such
# that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# EXAMPLE:
# num = [-1, 0, 1, 2, -1, -4] -> [
#                                   [-1, 0, 1],
#                                   [-1, -1, 2],
#                                ]

# INPUT:
# A list with integers

# OUTPUT:
# A list will all the sets of three elements that have a sum of 0

nums = [0,0,0,0]
nums1 = [-1,0,1,2,-1,-4]
print()

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC: Loop through the list and using the current num and using the
# twoSum technique in the rest fo the list (two pointers technique)

def threeSum(nums):
    size = len(nums)
    K = 3

    if size < K:
        return list()

    result = []
    nums = sorted(nums)
    current = []

    for i in range(size - K + 1):
        if not i or (nums[i] > nums[i-1]):
            target = 0 - nums[i]
            low = i + 1
            high = size - 1
            while low < high:
                twoSum = nums[low] + nums[high]
                if twoSum == target:
                    result.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low+1]: low += 1
                    while low < high and nums[high] == nums[high-1]: high -= 1
                    low += 1
                    high -= 1
                elif twoSum > target:
                    high -= 1
                else:
                    low += 1
    return result

print("Input:", nums)
print(threeSum(nums))
print()

print("Input:", nums1)
print(threeSum(nums1))
print()