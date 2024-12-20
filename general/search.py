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