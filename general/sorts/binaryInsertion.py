# Binary insertion sort combines binary search and insertion sort

# December 25th, 2024

# def binaryInsertionSort(array):

#     def binarySearch(left, right, target):
#         while left <= right:
#             midpoint = left + (right - left) // 2
#             midpointValue = array[midpoint]

#             if target < midpointValue:
#                 right = midpoint - 1

#             else:
#                 left = midpoint + 1

#         return left
    
#     for i in range(1, len(array)):
#         target = array[i]
#         insertPosition = binarySearch(0, i - 1, target)

#         for j in range(i, insertPosition, -1):
#             array[j] = array[j-1]

#         array[insertPosition] = target

#     return array
        

# print(binaryInsertionSort([6,3,8,3,1,6]))

# ---------------------------------------------------------------------------------------------

# def binaryInsertionSort(array):

#     def binarySearch(left, right, target):
#         while left <= right:
#             midpoint = left + (right - left) // 2
#             midpointValue = array[midpoint]

#             if target < midpointValue:
#                 right = midpoint - 1
#             else:
#                 left = midpoint + 1

#         return left
    
#     for i in range(1, len(array)):
#         target = array[i]
#         insertionPosition = binarySearch(0, i-1, target)

#         for j in range(i, insertionPosition, -1):
#             array[j] = array[j-1]

#         array[insertionPosition] = target

#     return array

# print(binaryInsertionSort([6,3,8,3,1,6]))

# -----------------------------------------------------------------------------------------

# def binaryInsertionSort(array):

#     def binarySearch(left, right, target):
#         while left <= right:
#             midpoint = left + (right - left) // 2
#             midpointValue = array[midpoint]

#             if target < midpointValue:
#                 right = midpoint - 1

#             else:
#                 left = midpoint + 1

#         return left
    
#     for i in range(1, len(array)):
#         target = array[i]
#         indexValue = binarySearch(0, i-1, target)

#         for j in range(i, indexValue, -1):
#             array[j] = array[j-1]

#         array[indexValue] = target

#     return array

# print(binaryInsertionSort([6,3,8,3,1,6]))

# --------------------------------------------------------------------------------------------
# December 26th, 2024

# def binaryInsertionSort(array):

#     def binarySearch(left, right, target):
#         while left <= right:
#             midpoint = left + (right - left) // 2
#             midpointValue = array[midpoint]

#             if target <= midpointValue:
#                 right = midpoint - 1

#             else:
#                 left = midpoint + 1

#         return left
    
#     for i in range(1, len(array)):
#         target = array[i]
#         insertionPosition = binarySearch(0, i, target)

#         for j in range(i, insertionPosition, -1):
#             array[j] = array[j-1]

#         array[insertionPosition] = target

#     return array

# print(binaryInsertionSort([6,3,8,3,1,6]))

# ---------------------------------------------------------------------------------------------
# December 27th, 2024

# def binaryInsertionSort(array):
#     def binarySearch(left, right, target):
#         while left < right:
#             midpoint = left + (right - left) // 2
#             midpointValue = array[midpoint]

#             if target < midpointValue:
#                 right = midpoint - 1
#             else:
#                 left = midpoint + 1

#         return left
    
#     for i in range(1, len(array)):
#         target = array[i]
#         posValue = binarySearch(0, i, target)

#         for j in range(i, posValue, -1):
#             array[j] = array[j-1]

#         array[posValue] = target

#     return array

# print(binaryInsertionSort([6,3,8,3,1,6]))

# --------------------------------------------------------------------------------------------
# December 28th, 2024

# def binaryInsertionSort(array):

#     def binarySearch(left, right, target):
#         while left < right:
#             midpoint = left + (right - left) // 2
#             midpointValue = array[midpoint]

#             if target < midpointValue:
#                 right = midpoint - 1

#             else:
#                 left = midpoint + 1

#         return left
    
#     for i in range(1, len(array)):
#         target = array[i]
#         position = binarySearch(0, i, target)

#         for j in range(i, position, -1):
#             array[j] = array[j-1]

#         array[position] = target
    
#     return array


# print(binaryInsertionSort([6,3,8,3,1,6]))

# ---------------------------------------------------------------------------------------------
# January 4th, 2024

# def binaryInsertionSort(array):

#     def binarySearch(left, right, target):
#         while left < right:
#             midpoint = left + (right - left) // 2
#             midpointValue = array[midpoint]

#             if target < midpointValue:
#                 right = midpoint - 1
            
#             else:
#                 left = midpoint + 1
        
#         return left

#     for i in range(1, len(array)):
#         target = array[i]
#         position = binarySearch()

# ----------------------------------------------------------------------------------------------





