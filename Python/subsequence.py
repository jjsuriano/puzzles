# NAME: 
# Subsequence

# DESCRIPTION: 
# Determine if str2 is a subsequence of str1.
# A subsequence means that a string is formed by deleting some characters (or 
# none) without distubing the positions of the characaters in the original 
# string.

# EXAMPLE:
# 'cod' and 'coin' are subsequences of 'coding'
# 'cxn' and 'ion' are not subsequences of 'coding'


# INPUT: 
# Two strings (str1 and str2)

# OUTPUT: 
# True or False if str2 is a subsequence of str1

str1 = 'coding'
str2 = 'coin'

print()

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC: 
# A solution that uses a dictionary to store the positions of each letter in 
# str1, then use that dictionary to determine if str2 is a subsequence.

def subsequence_1(str1, str2):

    positions = { c:i for i, c in enumerate(str1) }
    last_index = -1

    for c in str2:
        try: 
            index = positions[c]
        except KeyError:
            return False

        if index <= last_index:
            return False
        
        last_index = index

    return True

print(subsequence_1(str1, str2))
print()

# METHOD 2 - - - - -

print('METHOD 2')

# LOGIC:
# A solution that uses two pointers (one in str1 and the other one in str2) and 
# loops through the strings to determine if str2 is a subsequence.

def subsequence_2(str1, str2):

    i = 0
    j = 0

    while j < len(str2):

        c1 = str1[i]
        c2 = str2[j]

        if c1 == c2:
            j += 1
        
        i += 1

        if i == len(str1) and j < len(str2):
            return False
    
    return True

print(subsequence_2(str1, str2))
print()