# DESCRIPTION:
# Given a string S and a string T, find the minimum window in S which will contain all the characters in T.

# EXAMPLE:
# s = "ADOBECODEBANCM", t = "ABC" -> ("BANC", 4)

# INPUT: 
# Two strings s and t

# OUTPUT: 
# The minimum window in S that contains all the characters in T and the length of the minimum window

# METHOD 1 - - - - -
print('METHOD 1')

# LOGIC: 
# Use brute force by checking all the substrings in s

def minWindowSubstring(s, t):
  size_s = len(s)
  size_t = len(t)

  if size_s < size_t:
    return ("", 0)

  window = ""
  result = ""

  def checker():
    if len(window) < size_t:
      return False
    for i in t: 
      if i not in window:
        return False
    return True

  for i in range(size_s + 1):
    for j in range(i + 1, size_s + 1):
      window = s[i:j]
      if checker():
        if not result or len(result) > j-i:
          result = window
  return (result, len(result))

s = "ADOBECODEBANCM"
t = "ABC"
print(s, t)
print(minWindowSubstring(s, t))

print()

t = "SD"
print(s, t)
print(minWindowSubstring(s, t))

print()

t = "ONE"
print(s, t)
print(minWindowSubstring(s, t))

# METHOD 2 - - - - -
print('\nMETHOD 2')

# LOGIC: 
# Use the sliding window technique to traverse s only once (dynamic window)

def minWindowSubstring(s, t):
  size_s = len(s)
  size_t = len(t)

  if size_s < size_t:
    return ("", 0)

  from collections import defaultdict

  left, right = 0, 0
  window = defaultdict(int)
  result = ""

  def checker():
    for i in t:
      if not window[i]:
        return False
    return True

  while right < size_s:
    current_char = s[right]
    window[current_char] += 1
    right += 1

    while checker():
      if not result or len(result) > right-left:
        result = s[left:right]
      window[s[left]] -= 1
      left += 1

  return (result, len(result))

s = "ADOBECODEBANCM"
t = "ABC"
print(s, t)
print(minWindowSubstring(s, t))

print()

t = "SD"
print(s, t)
print(minWindowSubstring(s, t))

print()

t = "ONE"
print(s, t)
print(minWindowSubstring(s, t))