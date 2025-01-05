# December 20th, 2024
'''
O(n log n), optimal running time for comparison based algorithms
Breaks down problem recursively
Constantly splits in half
Divide and conquer principal
Length of array check has to be greater than 1
'''

# def mergeSort(array):
#     if len(array) > 1:
#         leftArray = array[:len(array)//2] # Grabs the left side of the array
#         rightArray = array[len(array)//2:]

#         # Recursion
#         mergeSort(leftArray)
#         mergeSort(rightArray)

#         # Merge
#         i = 0 # Left most element in left array index
#         j = 0 # Left most element in right array index
#         k = 0

#         while i < len(leftArray) and j < len(rightArray):
#             if leftArray[i] < rightArray[j]:
#                 array[k] = leftArray[i]
#                 i += 1
#             else:
#                 array[k] = rightArray[j]
#                 j += 1
#             k += 1
    
#         while i < len(leftArray):
#             array[k] = leftArray[i]
#             i += 1
#             k += 1

#         while j < len(rightArray):
#             array[k] = rightArray[j]
#             j += 1
#             k += 1

#         return array
    
#     else:
#         return array

# arrayTest = [2,3,5,1,7,4,4,4,2,6,0]
# nice = mergeSort(arrayTest)
# print(nice)

# --------------------------------------------------------------------------------------------------------------
# December 20th, 2024

# def mergeSort(array):
#     if len(array) > 1:
#         left = array[:len(array)//2]
#         right = array[len(array)//2:]

#         mergeSort(left)
#         mergeSort(right)

#         i = 0
#         j = 0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i += 1

#             else:
#                 array[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1

#         return array

#     else:
#         return 1

# arrayNew = [9,2,5,3,0,5,8,1,4,2,6,7,3,8,9,4]
# nice = mergeSort(arrayNew)
# print(nice)

# -------------------------------------------------------------

# def mergeSort(array):
#     if len(array) > 1:
#         left = array[:len(array)//2]
#         right = array[len(array)//2:]

#         mergeSort(left)
#         mergeSort(right)

#         i = 0
#         j = 0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i += 1
#             else:
#                 array[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1

#         return array
    
#     else:
#         return array

# glonk = [2,7,4,3,7,6]
# nice = mergeSort(glonk)
# print(nice)

# -------------------------------------------------------------------------------

# def mergeSort(array):
#     if len(array) > 1:
#         left = array[:len(array)//2]
#         right = array[len(array)//2:]

#         mergeSort(left)
#         mergeSort(right)

#         i = 0
#         j = 0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i += 1
#             else:
#                 array[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1
        
#         return array
#     else:
#         return array

# chlob = [2,5,4,3,988,7,5,9,0]
# print(mergeSort(chlob))

# --------------------------------------------------------------

# def mergeSort(array):
#     if len(array) > 1:
#         left = array[:len(array)//2]
#         right = array[len(array)//2:]

#         mergeSort(left)
#         mergeSort(right)

#         i = 0
#         j = 0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i += 1
#             else:
#                 array[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1
        
#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1
        
#         return array

#     else:
#         return array
 
# chlob = [2,5,4,3,988,7,5,9,0]
# print(mergeSort(chlob))

# ----------------------------------------------------------
# December 21st, 2024

# def mergeSort(array):
#     if len(array) > 1:
#         left = array[:len(array)//2]
#         right = array[len(array)//2:]

#         mergeSort(left)
#         mergeSort(right)

#         i = 0
#         j = 0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i += 1
#             else:
#                 array[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1
        
#         return array
    
#     else:
#         return array

# chlob = [2,5,4,3,988,7,5,9,0]
# print(mergeSort(chlob))

# -------------------------------------------------------------------------------------

# def mergeSort(array):
#     if len(array) > 1:
#         left = array[:len(array)//2]
#         right = array[len(array)//2:]

#         mergeSort(left)
#         mergeSort(right)

#         i = 0
#         j = 0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i += 1
#             else:
#                 array[k] = right[j]
#                 j += 1
#             k += 1
        
#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1
        
#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1
        
#         return array
#     else:
#         return array
    
# print(mergeSort([6,3,8,3,2,1,0,0,4]))

# ----------------------------------------------------------------------

# def mergeSort(array):
#     if len(array) > 1:
#         left = array[:len(array)//2]
#         right = array[len(array)//2:]

#         mergeSort(left)
#         mergeSort(right)

#         i = 0
#         j = 0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i += 1
#             else:
#                 array[k] = right[j]
#                 j += 1
#             k += 1
        
#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1
        
#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1

#         return array
#     else:
#         return array
    
# print(mergeSort([6,3,8,3,2,1,0,0,4]))

# --------------------------------------------------------------------------------------------
# Decemeber 22nd, 2024

# def mergeSort(array):
#     if len(array) > 1:
#         left = array[:len(array)//2]
#         right = array[len(array)//2:]

#         mergeSort(left)
#         mergeSort(right)

#         i = 0
#         j = 0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i += 1
#             else:
#                 array[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1
        
#         return array
#     else:
#         return array

# print(mergeSort([6,3,8,3,2,1,0,0,4]))

# ----------------------------------------------------------------------------------

# def mergeSort(array):
#     if len(array) > 1:
#         left = array[:len(array)//2]
#         right = array[len(array)//2:]
    
#         mergeSort(left)
#         mergeSort(right)

#         i = 0
#         j = 0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i += 1
#             else:
#                 array[k] = right[j]
#                 j += 1
#             k += 1
        
#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1
        
#         return array

#     else:
#         return array 

# print(mergeSort([6,3,8,3,2,1,0,0,4]))

# ---------------------------------------------------------------------------------------
# December 23rd, 2024

# def mergeSort(array):
#     if len(array) > 1:
#         left = array[:len(array)//2]
#         right = array[len(array)//2:]

#         mergeSort(left)
#         mergeSort(right)

#         i = 0
#         j = 0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i += 1
#             else:
#                 array[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1

#         return array
    
#     else:
#         return array


# print(mergeSort([6,3,8,3,2,1,0,0,4]))

# ---------------------------------------------------------------------------------------------
# December 24th, 2024

# def mergeSort(array):
#     if len(array) > 1:
#         left = array[:len(array)//2]
#         right = array[len(array)//2:]

#         mergeSort(left)
#         mergeSort(right)

#         i = 0
#         j = 0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i += 1
#             else:
#                 array[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1

#         return array

#     else:
#         return array

# print(mergeSort([6,3,8,3,2,1,0,0,4]))

# -----------------------------------------------------------------------------------------------

# def mergeSort(array):
#     if len(array) > 1:
#         left = array[:len(array)//2]
#         right = array[len(array)//2:]

#         mergeSort(left)
#         mergeSort(right)

#         i = 0
#         j = 0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i += 1
#             else:
#                 array[k] = right[j]
#                 j += 1
#             k += 1
        
#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1
#         return array
#     else:
#         return array

# print(mergeSort([6,3,8,3,2,1,0,0,4]))

# ----------------------------------------------------------------------------------------

# def mergeSort(array):
#     if len(array) > 1:
#         left = array[:len(array)//2]
#         right = array[len(array)//2:]

#         mergeSort(left)
#         mergeSort(right)

#         i = 0
#         j = 0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i += 1
#             else:
#                 array[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1

#         return array
    
#     else:
#         return array

# print(mergeSort([6,3,8,3,2,1,0,0,4]))

# ---------------------------------------------------------------------------------------
# December 26th, 2024

# def merge(array):
#     if len(array) > 1:
#         left = array[:len(array)//2]
#         right = array[len(array)//2:]

#         merge(left)
#         merge(right)

#         i = 0
#         j = 0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i += 1
#             else:
#                 array[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1
        
#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1

#         return array

#     else:
#         return array

# print(merge([6,3,8,3,2,1,0,0,4]))

# ----------------------------------------------------------------------------------------------
# January 4th, 2024

# def merge(array):
#     if len(array) > 1:
#         left = array[:len(array)//2]
#         right = array[len(array)//2:]

#         merge(left)
#         merge(right)

#         i = 0
#         j = 0
#         k = 0

#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 array[k] = left[i]
#                 i += 1
#             else:
#                 array[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             array[k] = left[i]
#             i += 1
#             k += 1
        
#         while j < len(right):
#             array[k] = right[j]
#             j += 1
#             k += 1

#         return array
#     else:
#         return array

# print(merge([6,3,8,3,2,1,0,0,4]))

# -----------------------------------------------------------------------------------------------













