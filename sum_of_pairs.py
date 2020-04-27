# Puzzle description: 
# Find how many pairs have the sum equal to the variable 'sum' in a given
# list of numbers.

numbers = [5, 1, 3, 7, 4, 2, 2, 1, 3, 6, -2]
sum = 7

# METHOD 1 - - - - -
print('METHOD 1')

pairs = []
used = []

# loop through the array
for i, x in enumerate(numbers):
    # loop through the array again in order to calculate the sum of both numbers
    for j, y in enumerate(numbers): 
        # check if the sum of those two elements matches the required sum
        # check if the elements we are comparing are not the same elements
        # check if we already used those numbers in those indeces to avoid duplicates
        # I used De Morgan's Law three times
        if not(x+y != sum or (i == j or (i in used or j in used))):
            # add the pair to the pairs array
            print(x, y)
            pairs.append((x, y))
            used.append(i)
            used.append(j)
            #break the inside loop to avoid duplicating if there is another 'y' later in the numbers array
            break 
# find out the number of pairs that match the sum
print('The number of pairs that have a sum of {} is {}.'.format(sum, len(pairs)))
print()

# METHOD 2 - - - - -
print('METHOD 2')

frequency = {}
counter = 0

# loop trhough the array to find out the frequencies of each value
# the key of the dictionary is the value in the array
# the value of that key is the frequency of the value in the array
for i in numbers: 
    # add the value to the dictionary if it is not in the dictionary
    if i not in frequency: 
        frequency[i] = 1
    # update the frequency by adding one if the value was already registered
    else: 
        frequency[i] += 1

# loop through the frequencies to count the number of pairs that have the sum we were asked for
for i in frequency:
    # find the difference between the value and the sum
    find = sum - i

    # check if i and find are the same
    if i == find and frequency[i] == 1:
        # continue if the frequency is 1 (you need two to make it work)
        continue
    # check if the value is in the dictionary
    # check if the frequency is not 0 for either value (helps avoid duplicates)
    if find in frequency and frequency[find] != 0 and frequency[i] != 0:
        print(i, find)
        # add 1 to the counter as a pair has been found
        counter += 1
        # decrease the frequency by 1 in order to avoid duplicates
        frequency[find] -= 1
        frequency[i] -= 1

print('The number of pairs that have a sum of {} is {}.'.format(sum, counter))
print()
