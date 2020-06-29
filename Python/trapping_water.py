"""
Trapping Water.

Given n non-negative integers representing an elevation map where the width
of each bar is 1, compute how much water it is able to trap after raining.

EXAMPLE:
[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1] -> 6
"""

print()

# METHOD 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1')


def trapped_water_area(elevation):
    """
    Calculate the area of the water trapped.

    LOGIC:

    INPUT:
    elevation: a list of the elevations

    OUTPUT:
    An integer of the area of the trapped water by the elevations
    """
    pass


TEST_A = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

RESULT_A = trapped_water_area(TEST_A)

CORRECT_A = 6

print("Testing A: ", end="")
print("OK" if RESULT_A == CORRECT_A
      else "FAIL (" + str(RESULT_A) + " vs " + str(CORRECT_A) + ")")

print()
