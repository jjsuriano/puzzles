# NAME: 
# Container with most water

# DESCRIPTION: 
# Find the container with the highest area from an array of heights (the height is given as an element in the array and the width is the difference between the two indexes of those two heights).

# INPUT: 
# An array of heights

# OUTPUT: 
# The max area

heights = [1,3,2,0,5,2,5,4,1,2]

# Expected solution: 18 sq units

# METHOD 1 - - - - -
print('METHOD 1')

max_area = 0

# loop through the heights array
for i, h1 in enumerate(heights): 
    # loop through the heights array again to calculate the max area
    for j, h2 in enumerate(heights):
        # ignore if the two values of the iterations are the same
        if i != j:
            # find the lowest height between the two values as that's the height used to calculate the area
            lowest = min(h1, h2)

            # calulate the current area with the distance between the indices and the height calculated above
            current_area = lowest * abs(i-j)

            # if the current area is bigger than the max area, set the max area to the current area
            if current_area > max_area:
                max_area = current_area

                #save some information to print the result
                indices = (i, j)
                x = abs(i-j)
                y = lowest

print('The container with the most water has an area of {} sq units.'.format(max_area))
print('With height of {} and width of {} (from index {} to index {}).'.format(y,x, indices[0], indices[1]))

print()

# METHOD 2 - - - - -
print('METHOD 2')



print()