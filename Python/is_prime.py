# DESCRIPTION:
# Given an int, check if the input is a prime number or not.

# EXAMPLE:
# 31 -> true
# 12 -> false

# INPUT:
# An int

# OUTPUT:
# A bool, true if the input is a prime number, false if it is a composite number

print()

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC:
# A prime number has only two factors 1 and itself. Loop through smaller numbers
# than num and check if num is divisible by any of those.

# To improve the efficiency of the function I:
# - return true if it is 2 (the only prime even number)
# - returned false immediately if num is even or 1
# - looped only through odd numbers
# - looped until num//i is greater than 1 because we are never going to reach 1 in
#   num//i because the only result that gives us 1 is num/num and the loop ends in
#   the odd number before num. Once the quotient reaches 1, there is no point in
#   running the loop.

def isPrime(x:int) -> bool:

    if x == 2:
        return True
    if x%2 == 0 or x == 1:
        return False
    i = 3
    while x//i > 1:
        if x%i == 0 and x != i:
            return False
        i += 2
    return True

print()

# print from 1 to 30 and determine if they are prime or not
for num in range(1, 31):
    if isPrime(num):
        print('{} is a prime number.'.format(num))
    else:
        print('{} is NOT a prime number.'.format(num))

print()