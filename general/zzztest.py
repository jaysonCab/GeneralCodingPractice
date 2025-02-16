# # Decemeber 20th, 2024
# # You can swap items in an array like this thats pretty cool
# listing = [2,4]
# listing[0], listing[1] = listing[1], listing[0]
# print(listing)

# December 21st, 2024

# array = [1,2,3,4]
# for i in range(len(array)):
#     print(i)

# December 22nd, 2024
# Cases?

# sheesh = int(input('Enter a number below 10: '))

# match sheesh:
#     case -1:
#         print('negative 1 is crazy')

#     case _ if 0 <= sheesh <= 10:
#         print(f'Your number was {sheesh}')
    
#     case _:
#         print('nothing gap')

# -----------------------------------------------------

# array = [7,3,8,4]
# array.sort()
# array.reverse()
# print(array)

# -------------------------------------------------------------------------
# December 30th, 2024

# string = '2 23 * 5 4 * + 9 -'
# array = string.split(' ')
# print(array)

# -------------------------------------------------------------------------

# stack = 'abcde'
# print(stack[:-1])

# dictionary = {
#     ')': '('
# }
# sett = ')'
# for i in range(1):
#     print(dictionary[sett[i]])

# -------------------------------------------------------------------------------------------------------
# January 2nd, 2024

# from collections import Counter

# def is_permutation(s1, s2):
#     if len(s1) != len(s2):
#         return False
#     if Counter(s1) == Counter(s2):
#         return True
#     else:
#         return False

# # Test
# print(is_permutation("abc", "cab"))  # True
# print(is_permutation("abc", "def"))  # False

# string = 'abc'
# string = string[1:]
# print(string)
# string2 = 'abcdefg'
# for i in range(len(string), len(string2)):
#     print(string2[i])

# ----------------------------------------------------------------------------------------------------------------
# February 15th, 2025

diction = {
    "apple": 2,
    "pear": 3
}

print(diction["apple"] + diction["pear"])