# December 20th 2024
# minus 1 in range since the final item will always be sorted

# def selection(array):
#     for i in range(len(array)-1):
#         currentMinimum = i

#         for j in range(i+1, len(array)):
#             if array[j] < array[currentMinimum]:
#                 currentMinimum = j

#         array[i], array[currentMinimum] = array[currentMinimum], array[i]

#     return array

# listing = [4,2,7,1,8,4,2,3,0,9,8]
# print(selection(listing))

# ------------------------------------------------------------------------------

# def selectionSort(array):
#     for i in range(len(array)-1):
#         currentMinimum = i

#         for j in range(i+1, len(array)):
#             if array[j] < array[currentMinimum]:
#                 currentMinimum = j
        
#         array[i], array[currentMinimum] = array[currentMinimum], array[i]
    
#     return array

# listing = [4,2,7,1,8,4,2,3,0,9,8]
# print(selectionSort(listing))

# -----------------------------------------------------------------------------
# December 21st

# def selectionSort(array):
#     for i in range(len(array)-1):
#         currentMinimum = i

#         for j in range(i+1, len(array)):
#             if array[j] < array[currentMinimum]:
#                 currentMinimum = j

#         array[i], array[currentMinimum] = array[currentMinimum], array[i]
#     return array

# listing = [4,2,7,1,8,4,2,3,0,9,8]
# print(selectionSort(listing))

# -------------------------------------------------------------------------------------

# def selectionSort(array):
#     for i in range(len(array)-1):
#         currentMinimum = i

#         for j in range(i + 1, len(array)):
#             if array[j] < array[currentMinimum]:
#                 currentMinimum = j

#         array[i], array[currentMinimum] = array[currentMinimum], array[i]

#     return array
        
# listing = [4,2,7,1,8,4,2,3,0,9,8]
# print(selectionSort(listing))

# ------------------------------------------------------------------------------------

# def selectionSort(array):
#     for i in range(len(array)-1):
#         currentMin = i

#         for j in range(i+1, len(array)):
#             if array[j] < array[currentMin]:
#                 array[j], array[currentMin] = array[currentMin], array[j]
    
#     return array

# listing = [4,2,7,1,8,4,2,3,0,9,8]
# print(selectionSort(listing))

# ---------------------------------------------------------------------------------