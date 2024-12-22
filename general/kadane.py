# December 21st, 2024

# def kanadeMax(array):
#     maxSum = float('-inf')
#     currentMax = 0

#     for i in range(len(array)):
#         currentMax += array[i]
#         maxSum = max(maxSum, currentMax)

#         if currentMax < 0:
#             currentMax = 0

#     return maxSum

# test_array = [-2, 3, -1, 2, -3, 5, -2, 4, -1, 6]
# print(kanadeMax(test_array))

# ----------------------------------------------------------------------------------

# def kadaneGrab(nums):
#         maxSum = float('-inf')
#         current = 0

#         for i in range(len(nums)):
#             current += nums[i]
#             maxSum = max(current, maxSum)

#             if current < 0:
#                 current = 0

#         return maxSum

# test_array = [-2, 3, -1, 2, -3, 5, -2, 4, -1, 6]
# print(kadaneGrab(test_array))

# --------------------------------------------------------------------------------------
