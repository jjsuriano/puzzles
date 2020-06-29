"""
Container with Most Water.

Find the container with the highest area from an array of heights (the height
is given as an element in the array and the width is the difference between
the two indexes of those two heights).

EXAMPLE:
heights = [1, 3, 2, 0, 5, 2, 5, 4, 1, 2] -> 18
"""

print()

# METHOD 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1')


def max_area(heights):
    """
    Calculate the maximum area with the given heights.

    LOGIC:
    A brute force solution that finds every area possible and determine the max
    area

    INPUT:
    An array of heights (heights)

    OUTPUT:
    The max area
    """
    result = 0

    for i in range(0, len(heights)):
        for j in range(i+1, len(heights)):
            if i != j:
                lowest = min(heights[i], heights[j])
                current_area = lowest * (j-i)
                result = max(result, current_area)

    return result


# TEST CASES
TEST_A = [1, 3, 2, 0, 5, 2, 5, 4, 1, 2]

RESULT_A = max_area(TEST_A)

CORRECT_A = 18

print("Testing A: ", end="")
print("OK" if RESULT_A == CORRECT_A
      else "FAIL (" + str(RESULT_A) + " vs " + str(CORRECT_A) + ")")

print()

# METHOD 2 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 2')


def max_area(heights):
    """
    Calculate the maximum area with the given heights.

    LOGIC:
    Use two pointers (one at the start and one at the end of the array),
    calculate the area of these two pointers, move the pointer with the
    shortest height closer to the middle until they meet.

    INPUT:
    heights: an array of heights

    OUTPUT:
    The max area
    """
    result = 0
    i = 0
    j = len(heights) - 1

    while i < j:
        width = j - i
        left = heights[i]
        right = heights[j]

        if left <= right:
            current_area = left * width
            i += 1
        else:
            current_area = right * width
            j -= 1

        result = max(result, current_area)

    return result


# TEST CASES
RESULT_A = max_area(TEST_A)

print("Testing A: ", end="")
print("OK" if RESULT_A == CORRECT_A
      else "FAIL (" + str(RESULT_A) + " vs " + str(CORRECT_A) + ")")
print()
