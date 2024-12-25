# December 24th, 2024

# TEST 1
# You can create sets in two different ways
# You can't do set1 = {}, this will make it think that its a dicitonary
print('TEST 1, creating sets')

set1 = set()
set1.add(5)
print(set1)

set2 = {1,4}
set2.add(4)
print(f'{set2}\n')

# ------------------------------

# TEST 2
# UNION |
# This will return all unique numbers found in both sets
print('TEST 2, union of sets')

set1 = {1,3,5}
set2 = {2,4,6}

set3 = set1 | set2
print(f'{set3}\n')

# ------------------------------

# TEST 3
# AND &
# This will return all unique numbers that are shared across both sets
print('TEST 3, and function')

set1 = {1,3,5}
set2 = {1,4,6}

set3 = set1 & set2
print(f'{set3}\n')

# ------------------------------

# TEST 4
# DIFFERENCE -             I think this is also inverse
# This will return all the unique numbers that are not shared across both sets but the primary is the left set
# ORDER MATTERS
print('TEST 4, difference function')

set1 = {2,4,5}
set2 = {1,2,4}

set3 = set1 - set2
print(f'{set3}\n')

# -----------------------------

# TEST 5
# SYMETRIC DIFFERENCE ^
# This will return all the unique numbers that are in the first AND second set, but eliminate all that are same
print('TEST 5, symetric differnece')

set1 = {2,4,5}
set2 = {1,2,4}

set3 = set1 ^ set2
print(f'{set3}\n')


