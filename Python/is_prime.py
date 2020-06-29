"""
Is Prime.

Given an int, check if the input is a prime number or not.

EXAMPLE:
31 -> true
12 -> false
"""

print()

# METHOD 1 - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
print('METHOD 1')


def is_prime(x: int) -> bool:
    """
    Determine if a number is a prime number or not.

    LOGIC:
    A prime number has only two factors 1 and itself. Loop through smaller
    numbers than num and check if num is divisible by any of those.

    To improve the efficiency of the function I:
    - return true if it is 2 (the only prime even number)
    - returned false immediately if num is even or 1
    - looped only through odd numbers
    - looped until num//i is greater than 1 because we are never going to reach
    1 in num//i because the only result that gives us 1 is num/num and the loop
    ends in the odd number before num. Once the quotient reaches 1, there is no
    point in running the loop.

    INPUT:
    An int

    OUTPUT:
    A bool, true if the input is a prime number, false if it is a composite
    number
    """
    if x == 2:
        return True
    if x % 2 == 0 or x == 1:
        return False
    i = 3
    while x//i > 1:
        if x % i == 0 and x != i:
            return False
        i += 2
    return True


# TEST CASES
TEST_A = 7167
TEST_B = 234
TEST_C = 31
TEST_D = 29
TEST_E = 19997779

RESULT_A = is_prime(TEST_A)
RESULT_B = is_prime(TEST_B)
RESULT_C = is_prime(TEST_C)
RESULT_D = is_prime(TEST_D)
RESULT_E = is_prime(TEST_E)

CORRECT_A = False
CORRECT_B = False
CORRECT_C = True
CORRECT_D = True
CORRECT_E = True

print("Testing A: ", end="")
print("OK" if RESULT_A == CORRECT_A
      else "FAIL (" + str(RESULT_A) + " vs " + str(CORRECT_A) + ")")

print("Testing B: ", end="")
print("OK" if RESULT_B == CORRECT_B
      else "FAIL (" + str(RESULT_B) + " vs " + str(CORRECT_B) + ")")

print("Testing C: ", end="")
print("OK" if RESULT_C == CORRECT_C
      else "FAIL (" + str(RESULT_C) + " vs " + str(CORRECT_C) + ")")

print("Testing D: ", end="")
print("OK" if RESULT_D == CORRECT_D
      else "FAIL (" + str(RESULT_D) + " vs " + str(CORRECT_D) + ")")

print("Testing E: ", end="")
print("OK" if RESULT_E == CORRECT_E
      else "FAIL (" + str(RESULT_E) + " vs " + str(CORRECT_E) + ")")

print()

# print from 1 to 30 and determine if they are prime or not
print("Testing numbers 1 to 30:")
for num in range(1, 31):
    if num == 30:
        ending = ".\n"
    elif not num % 10:
        ending = ",\n"
    else:
        ending = ", "

    if is_prime(num):
        print(f'{num} (PRIME)', end=ending)
    else:
        print(f'{num}', end=ending)

print()
