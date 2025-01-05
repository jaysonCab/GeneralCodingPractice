# Binary search algorithm: Takes a sorted list and finds the positional value or returns -1 if not found

# def binarySearch(sequence, item):
#     beginIndex = 0
#     endIndex = len(sequence) - 1

#     while beginIndex <= endIndex:
#         midpoint = beginIndex + (endIndex - beginIndex) // 2
#         midpointValue = sequence[midpoint]

#         if midpointValue == item:
#             return midpoint
        
#         elif item < midpoint:
#             endIndex = midpoint - 1

#         else:
#             beginIndex = midpoint + 1
    
#     return None

# sequence_a = [1,2,3,4,5,6,7,8,9]
# item_a = 7

# print(binarySearch(sequence_a, item_a))

# ------------------ Self attempt

# def binarySearch(orderedList, targetValue):
#     beginningValue = 0
#     endValue = len(orderedList) - 1

#     while beginningValue < endValue:
#         midpoint = beginningValue + (endValue - beginningValue) // 2
#         midpointValue = orderedList[midpoint]

#         if midpointValue == targetValue:
#             return midpoint
        
#         elif midpointValue > target:
#             endValue = midpoint - 1

#         else:
#             beginningValue = midpoint + 1
    
#     return -1

# listing = [1,23,52,99,102]
# target = 100
# indexValue = binarySearch(listing, target)

# print(indexValue)
# print(listing[indexValue])

# -----------------------------------------------------------------------------------

# def binarySearch(array, target):
#     left = 0
#     right = len(array) - 1

#     while left < right:
#         midpoint = left + (right - left) // 2
#         midpointValue = array[midpoint]

#         if target < midpointValue:
#             right = midpoint - 1
        
#         elif target > midpointValue:
#             left = midpoint + 1

#         elif target == midpointValue:
#             return midpoint
        
        
#     return -1


# arrayCheck = [1,4,6,77,88,99,192,248]
# nice = binarySearch(arrayCheck, 192)
# print(arrayCheck[nice])
# print(nice)

# -------------------------------------------------------
# December 20th, 2024

# def binarySearch(array, target):
#     left = 0
#     right = len(array) - 1

#     while left < right:
#         midpoint = left + (right - left) // 2
#         midpointValue = array[midpoint]

#         if target == midpointValue:
#             return midpoint
        
#         elif target < midpointValue:
#             right = midpoint - 1

#         else:
#             left = midpoint + 1

#     return -1

# sortedList = [1,3,36,55,63,92,104]
# target = 92
# nice = binarySearch(sortedList, target)
# print(nice)
# print(sortedList[nice])

# ---------------------------------------------------------

# def binarySearch(array, target):
#     left = 0
#     right = len(array) - 1

#     while left < right:
#         midpoint = left + (right - left) // 2
#         midpointValue = array[midpoint]

#         if target == midpointValue:
#             return midpoint
        
#         elif target < midpointValue:
#             right = midpoint - 1

#         else:
#             left = midpoint + 1
    
#     return -1

# shink = [1,2,3,4,5,6,7,8,9,10]
# glonk = 9

# nice = binarySearch(shink,glonk)
# print(nice)
# print(shink[nice])

# --------------------------------------------------------------

# def binarySearch(array, target):
#     left = 0
#     right = len(array) - 1

#     while left < right:
#         midpoint = left + (right - left) // 2
#         midpointValue = array[midpoint]

#         if target == midpointValue:
#             return midpoint
        
#         elif target < midpoint:
#             right = midpoint - 1
        
#         else:
#             left = midpoint + 1
    
#     return -1

# shink = [1,2,3,4,5,6,7,8,9,10]
# glonk = 9
# nice = binarySearch(shink,glonk)
# print(nice)
# print(shink[nice])

# ------------------------------------------------------
# December 21st, 2024

# def binarySearch(array, target):
#     left = 0
#     right = len(array) - 1

#     while left <= right:
#         middlepoint = left + (right - left) // 2
#         middlepointValue = array[middlepoint]

#         if target == middlepointValue:
#             return middlepoint
#         elif target < middlepointValue:
#             right = middlepoint - 1
#         else:
#             left = middlepoint + 1

#     return -1

# shink = [1,2,3,4,5,6,7,8,9,10]
# glonk = 9
# nice = binarySearch(shink,glonk)
# print(nice)
# print(shink[nice])

# -------------------------------------------------------------------------------

# def binarySearch(array, target):
#     left = 0
#     right = len(array) - 1

#     while left <= right:
#         midpoint = left + (right - left) // 2
#         midpointValue = array[midpoint]

#         if target == midpointValue:
#             return midpoint
        
#         elif target < midpointValue:
#             right = midpoint - 1
        
#         else:
#             left = midpoint + 1
    
#     return -1

# shink = [1,2,3,4,5,6,7,8,9,10]
# glonk = 4
# nice = binarySearch(shink,glonk)
# print(nice)
# print(shink[nice])

# ------------------------------------------------------------------------------------------
# December 22nd, 2024

# def binarySearch(array, target):
#     left = 0
#     right = len(array) - 1

#     while left <= right:
#         midpoint = left + (right - left) // 2
#         midpointValue = array[midpoint]

#         if midpointValue == target:
#             return midpoint
        
#         elif target < midpointValue:
#             right = midpoint - 1

#         else:
#             left = midpoint + 1

#     return -1

# shink = [1,2,3,4,5,6,7,8,9,10]
# glonk = 4
# nice = binarySearch(shink,glonk)
# print(nice)
# print(shink[nice])

# -------------------------------------------------------------------------------------------------

# def binarySearch(array, target):
#     left = 0
#     right = len(array) - 1

#     while left <= right:
#         midpoint = left + (right - left) // 2
#         valMidpoint = array[midpoint]

#         if valMidpoint == target:
#             return midpoint
        
#         elif valMidpoint > target:
#             right = midpoint - 1

#         else:
#             left = midpoint + 1

#     return -1

# shink = [1,2,3,4,5,6,7,8,9,10]
# glonk = 4
# nice = binarySearch(shink,glonk)
# print(nice)
# print(shink[nice])

# ------------------------------------------------------------------------------------------
# December 23rd, 2024

# def binarySearch(array, target):
#     left = 0
#     right = len(array) - 1

#     while left <= right:
#         midpoint = left + (right - left) // 2
#         midpointValue = array[midpoint]

#         if target == midpointValue:
#             return midpoint
        
#         elif target < midpointValue:
#             right = midpoint - 1

#         else:
#             left = midpoint + 1

#     return -1

# shink = [1,2,3,4,5,6,7,8,9,10]
# glonk = 11
# nice = binarySearch(shink,glonk)
# print(nice)
# print(shink[nice])

# --------------------------------------------------------------------------------------------
# December 24th, 2024

# def binarySearch(array, target):
#     left = 0
#     right = len(array) - 1

#     while left <= right:
#         midpoint = left + (right - left) // 2
#         midpointValue = array[midpoint]

#         if midpointValue == target:
#             return midpoint
        
#         elif target < midpointValue:
#             right = midpoint - 1

#         else:
#             left = midpoint + 1

#     return -1

# shink = [1,2,3,4,5,6,7,8,9,10]
# glonk = 7
# nice = binarySearch(shink,glonk)
# print(nice)
# print(shink[nice])

# ------------------------------------------------------------------------------------------------

# def binarySearch(array, target):
#     left = 0
#     right = len(array) - 1

#     while left <= right:
#         midpoint = left + (right - left) // 2
#         midpointvalue = array[midpoint]

#         if target == midpointvalue:
#             return midpoint
        
#         elif target < midpointvalue:
#             right = midpoint - 1

#         else:
#             left = midpoint + 1

#     return -1

# shink = [1,2,3,4,5,6,7,8,9,10]
# glonk = 7
# nice = binarySearch(shink,glonk)
# print(nice)
# print(shink[nice])

# ---------------------------------------------------------------------------------------------

# def binarySearch(array, target):
#     left = 0
#     right = len(array) - 1

#     while left <= right:
#         midpoint = left + (right - left) // 2
#         midpointValue = array[midpoint]

#         if target == midpointValue:
#             return midpoint
        
#         elif target < midpointValue:
#             right = midpoint - 1

#         else:
#             left = midpoint + 1
    
#     return -1

# shink = [1,2,3,4,5,6,7,8,9,10]
# glonk = 7
# nice = binarySearch(shink,glonk)
# print(nice)
# print(shink[nice])

# -----------------------------------------------------------------------------------------------
# December 25th, 2024

# def binarySearch(array, target):
#     left = 0
#     right = len(array) - 1

#     while left <= right:
#         midpoint = left + (right - left) // 2
#         midpointValue = array[midpoint]

#         if midpointValue == target:
#             return midpoint

#         elif target < midpointValue:
#             right = midpoint - 1

#         else:
#             left = midpoint + 1

#     return -1

# shink = [1,2,3,4,5,6,7,8,9,10]
# glonk = 7
# nice = binarySearch(shink,glonk)
# print(nice)
# print(shink[nice])

# ------------------------------------------------------------------------------------------
# December 26th, 2024

# def binarySearch(array, target):
#     left = 0
#     right = len(array) - 1

#     while left <= right:
#         midpoint = left + (right - left) // 2
#         midpointValue = array[midpoint]

#         if target == midpointValue:
#             return midpoint
        
#         elif target < midpointValue:
#             right = midpoint - 1

#         else:
#             left = midpoint + 1

#     return -1

# shink = [1,2,3,4,5,6,7,8,9,10]
# glonk = 9
# nice = binarySearch(shink,glonk)
# print(nice)
# print(shink[nice])

# --------------------------------------------------------------------------------------------
# December 28th, 2024

# def binarySearch(array, target):
#     left = 0
#     right = len(array) - 1

#     while left <= right:
#         midpoint = left + (right - left) // 2
#         midpointValue = array[midpoint]

#         if target == midpointValue:
#             return midpoint

#         elif target < midpointValue:
#             right = midpoint - 1

#         else:
#             left = midpoint + 1

# shink = [1,2,3,4,5,6,7,8,9,10]
# glonk = 9
# nice = binarySearch(shink,glonk)
# print(nice)
# print(shink[nice])

# --------------------------------------------------------------------------------------------
# January 4th, 2024

# def binarySearch(array, target):
#     left = 0
#     right = len(array) - 1

#     while left <= right:
#         midpoint = left + (right - left) // 2
#         midpointValue = array[midpoint]

#         if midpointValue == target:
#             return midpoint
    
#         elif target < midpointValue:
#             right = midpoint - 1
        
#         else:
#             left = midpoint + 1

#     return midpoint

# shink = [1,2,3,4,5,6,7,8,9,10]
# glonk = 9
# nice = binarySearch(shink,glonk)
# print(nice)
# print(shink[nice])

# -----------------------------------------------------------------------------------------------













