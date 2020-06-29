"""
N-bit Binaries.

Given a number N, print all the binary combinations with N bit.

EXAMPLE:
n = 1 -> "0", "1"
n = 2 -> "00", "01", "10", "11"
"""

print()

# METHOD 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1')


def n_bit_binaries(n):
    """
    Print all the binary combinations with n bits.

    LOGIC:
    Using recursion

    INPUT:
    n: the number of bits the results are going to have

    OUTPUT:
    All the possible bit combinations of N-bits
    """
    return _n_bit_binaries(n, "")


def _n_bit_binaries(n, output, result=None):
    if result is None:
        result = []

    if n == 0:
        result.append(output)
        return result

    _n_bit_binaries(n-1, output+"0", result)\
        + _n_bit_binaries(n-1, output+"1", result)

    return result


# TEST CASES
TEST_A = 2
TEST_B = 3
TEST_C = 1

RESULT_A = n_bit_binaries(TEST_A)
RESULT_B = n_bit_binaries(TEST_B)
RESULT_C = n_bit_binaries(TEST_C)

CORRECT_A = ["00", "01", "10", "11"]
CORRECT_B = ['000', '001', '010', '011', '100', '101', '110', '111']
CORRECT_C = ["0", "1"]

print("Testing A: ", end="")
print("OK" if RESULT_A == CORRECT_A
      else "FAIL (" + str(RESULT_A) + " vs " + str(CORRECT_A) + ")")

print("Testing B: ", end="")
print("OK" if RESULT_B == CORRECT_B
      else "FAIL (" + str(RESULT_B) + " vs " + str(CORRECT_B) + ")")

print("Testing C: ", end="")
print("OK" if RESULT_C == CORRECT_C
      else "FAIL (" + str(RESULT_C) + " vs " + str(CORRECT_C) + ")")

print()
