# NAME: 
# Container with most water

# DESCRIPTION: 
# Find the container with the highest area from an array of heights (the height 
# is given as an element in the array and the width is the difference between 
# the two indexes of those two heights).

# INPUT: 
# An array of heights (heights)

# OUTPUT: 
# The max area

heights = [1,3,2,0,5,2,5,4,1,2]

print()

# Expected solution: 18 sq units

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC: 
# A brute force solution that finds every area possible and determine the max 
# area.

max_area = 0

for i in range(0, len(heights)): 
    for j in range(i+1, len(heights)):
        if i != j:
            lowest = min(heights[i], heights[j])
            current_area = lowest * (j-i)
            max_area = max(max_area, current_area)

print('The container with the most water has an area of {} sq units.'.format(max_area))
print()

# METHOD 2 - - - - -
print('METHOD 2')

# LOGIC:
# Use two pointers (one at the start and one at the end of the array), calculate
# the area of these two pointers, move the pointer with the shortest height 
# closer to the middle until they meet.

max_area = 0
i = 0
j = len(heights) - 1

while i < j:    
    width = j-i
    left = heights[i]
    right = heights[j]

    if left <= right: 
        current_area = left * width
        i+=1
    else:
        current_area = right * width
        j-=1

    max_area = max(max_area, current_area)

print('The container with the most water has an area of {} sq units.'.format(max_area))
print()