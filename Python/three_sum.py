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
nums2 = [-1,0,1,2,-1,-4,-1,-1,-1,-1]
print()

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC: Loop through the list and using the current num and using the
# twoSum technique in the rest of the list (two pointers technique)

def threeSum(nums):
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

print("Input:", nums)
print(threeSum(nums))
print()

print("Input:", nums1)
print(threeSum(nums1))
print()

print("Input:", nums2)
print(threeSum(nums2))
print()

# METHOD 2 - - - - -
print('METHOD 2')

# LOGIC: Loop through the list and using the current num and using the
# twoSum technique in the rest of the list (dictionary)
# this uses MORE memory than METHOD 1

def threeSum(nums):
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

print("Input:", nums)
print(threeSum(nums))
print()

print("Input:", nums1)
print(threeSum(nums1))
print()

print("Input:", nums2)
print(threeSum(nums2))
print()