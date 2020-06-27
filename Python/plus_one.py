# DESCRIPTION: 
# The input is a non-empty array that represents the digits of a positive 
# integer, and the purpose is to return a non-empty array with the digits that 
# represent the same positive integer plus one.

# EXAMPLE:
# input: [1,2,3], output: [1,2,4]


# INPUT: 
# A non-empty array of integers that represent the digits of a non positive 
# integer (num)


# OUTPUT: 
# A non-empty array of integer that represent the digits of num plus one

num = [9,9,9]

print()

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC: 
# The last value in the array will be added 1 and the other elements will be 
# added the carry over from the last addition. The carry over value is 1 if the
# previous number resulted a 10. If at the end of the loop the carry is 1, 
# insert a 1 at the beginning of the array.

print('{} + 1 is equal to: '.format(num))

max_i = len(num) - 1
carry = 0

for i in range(max_i, -1, -1):
    
    if i == max_i:
        num[i] += 1
    else:
        num[i] += carry
        carry = 0

    if num[i] == 10:
        num[i] = 0
        carry = 1

if carry == 1:
    num.insert(0, 1)

print(num)
print()