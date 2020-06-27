# DESCRIPTION:
# Given a number N, print all the binary combinations with N bit.

# EXAMPLE:
# n = 1 -> "0", "1"
# n = 2 -> "00", "01", "10", "11"

# INPUT:
# N, the number of bits the results are going to have

# OUTPUT:
# All the possible bit combinations of N-bits

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC:
# A solution that uses recursion.

def nBitBinaries(n):
    _nBitBinaries(n, "")

def _nBitBinaries(n, output):
    if n == 0:
        print(output)
        return ""

    return _nBitBinaries(n-1, output+"0") + _nBitBinaries(n-1, output+"1")

nBitBinaries(2)