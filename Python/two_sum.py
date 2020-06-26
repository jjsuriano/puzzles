# DESCRIPTION:
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# EXAMPLE:
# num = [2, 7, 11, 15], target = 9 -> [0, 1]

# INPUT: 
# A list with integers

# OUTPUT: 
# The two indices of the numbers that have the sum of target

nums = [2, 7, 11, 15]
print()

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC: 
# Loop through all the numbers and add the difference (target - num) to a dictionary as a key and a value of i
# if the current num in the for loop is a key of the dictionary then return the value of dict[num] and i
# dict[num] has the index of the other number (target - num)

def twoSum(nums, target):
    indices = dict()

    for i, num in enumerate(nums): 
        if num in indices:
            return (indices[num], i)
        else: 
            indices[target - num] = i
    return None

target = 9
print(nums, "and a target of", target)
print(twoSum(nums, target))

print()

target = 10
print(nums, "and a target of", target)
print(twoSum(nums, target))
