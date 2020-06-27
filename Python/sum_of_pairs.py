# DESCRIPTION: 
# Find how many pairs have the sum equal to the variable 'sum' in a given list 
# of numbers. No duplicates are allowed (a value can be used only one time).

# INPUT: 
# An array of numbers (numbers) and the desired sum (sum)

# OUTPUT: 
# The number of pairs that match the sum when added

numbers = [1, 3, 4, 8, 2, 5]
sum = 5

print()

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC: 
# A brute force solution that adds up an element with another element to see if 
# they match the desired sum. 

pairs = []
used = []

for i in range(0, len(numbers)):
    for j in range(i+1, len(numbers)): 
        x = numbers[i]
        y = numbers[j]
        # I used De Morgan's Law
        if x+y == sum and not(i in used or j in used):
            pairs.append((x, y))
            used.append(i)
            used.append(j)
            break 

print('The number of pairs that have a sum of {} is {}.'.format(sum, len(pairs)))
print()

# METHOD 2 - - - - -
print('METHOD 2')

# LOGIC:
# This solution finds the number of times a number appears in the input list. 
# Using that frequency table, find the matching pairs that add up to 'sum'.

frequency = {}
counter = 0

for i in numbers: 
    if i not in frequency: 
        frequency[i] = 1
    else: 
        frequency[i] += 1

for i in frequency:
    find = sum - i

    if (i == find and frequency[i] <= 1):
        continue

    if find in frequency and frequency[find] != 0 and frequency[i] != 0:
        appearances = min(frequency[i], frequency[find])
        if find == i:
            appearances //= 2
        counter += appearances
        frequency[find] -= appearances
        frequency[i] -= appearances

print('The number of pairs that have a sum of {} is {}.'.format(sum, counter))
print()