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


def nBitBinaries(n):
    """
    Print all the binary combinations with n bits.

    LOGIC:
    Using recursion

    INPUT:
    N, the number of bits the results are going to have

    OUTPUT:
    All the possible bit combinations of N-bits
    """
    return _nBitBinaries(n, "")


def _nBitBinaries(n, output, result=None):
    if result is None:
        result = []

    if n == 0:
        result.append(output)
        return result

    _nBitBinaries(n-1, output+"0", result)\
        + _nBitBinaries(n-1, output+"1", result)

    return result


print(nBitBinaries(2))
