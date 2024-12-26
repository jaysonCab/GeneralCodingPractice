# RIGHT ROTATION is the simplest to understand, time complexity of O(n) and space complexity of O(1)

# ------------------------------------------------------------------------------------------
# This is how it works Right Rotation

# k %= 4
# 1 2 3 4 5 6 7

# reverse
# 7 6 5 4 3 2 1

# left = 0 right = k - 1
# 4-1 is position 3

# 4 5 6 7 3 2 1

# left = k right = len(array) - 1
# 4 5 6 7 1 2 3

#  ------------------------------------------------------------------------------------------
# December 25th, 2024

# def rotationRight(nums, k):
#     k %= len(nums)

#     def reversal(left, right):
#         while left < right:
#             nums[left], nums[right] = nums[right], nums[left]
#             left += 1
#             right -= 1
        
#     left, right = 0, len(nums) - 1
#     reversal(left, right)

#     left, right = 0, k - 1
#     reversal(left, right)

#     left, right = k, len(nums) - 1
#     reversal(left, right)

#     return nums

# nums = [1,2,3,4,5]
# k = 2
# print(rotationRight(nums, k))

# --------------------------------------------------------------------------------------------

# def rightRotation(array, k):
#     k %= len(array)

#     def reverse(left, right):
#         while left < right:
#             array[left], array[right] = array[right], array[left]
#             left += 1
#             right -= 1
        
#     left, right = 0, len(array) - 1
#     reverse(left, right)

#     left, right = 0, k - 1
#     reverse(left, right)

#     left, right = k, len(array) - 1
#     reverse(left, right)
    
#     return nums

# nums = [1,2,3,4,5]
# k = 5
# print(rightRotation(nums, k))

# --------------------------------------------------------------------------------------------
# December 26th, 2024

# def rightRotation(array, k):
#     k %= len(array)

#     def rotation(left, right):
#         while left < right:
#             array[left], array[right] = array[right], array[left]
#             left += 1
#             right -= 1

#     left, right = 0, len(array)-1
#     rotation(left, right)

#     left, right = 0, k-1
#     rotation(left, right)

#     left, right = k, len(array)-1
#     rotation(left,right)

#     return array

# nums = [1,2,3,4,5]
# k = 2
# print(rightRotation(nums, k))

# -----------------------------------------------------------------------------------------------












'''
Right Rotation Above

Left Rotation Below
'''

# -----------------------------------------------------------------------------------------------
# This is how Left Rotation works

# k %= len(array)
# so lets say k = 4

# 1 2 3 4 5 6 7 8 9

# reverse the first portion
# left = 0, right = k - 1
# 4 3 2 1 5 6 7 8 9

# reverse the second portion
# left = k, right = len(array) - 1
# 4 3 2 1 9 8 7 6 5

# reverse the entire thing
# left = 0, right = len(array) - 1
# 5 6 7 8 9 1 2 3 4

# -------------------------------------------------------------------------------------------
# December 25th, 2024

# def leftRotaiton(nums, k):
#     k %= len(nums)

#     def reverse(left, right):
#         while left < right:
#             nums[left], nums[right] = nums[right], nums[left]
#             left += 1
#             right -= 1

#     left, right = 0, k-1
#     reverse(left, right)

#     left, right = k, len(nums) - 1
#     reverse(left, right)

#     left, right = 0, len(nums) - 1
#     reverse(left, right)

#     return nums

# nums = [1,2,3,4,5]
# k = 1
# print(leftRotaiton(nums, k))

# ----------------------------------------------------------------------------------------------

# def leftRotation(nums, k):
#     k %= len(nums)

#     def reverse(left, right):
#         while left < right:
#             nums[left], nums[right] = nums[right], nums[left]
#             left += 1
#             right -= 1

#     left, right = 0, k - 1
#     reverse(left, right)

#     left, right = k, len(nums) - 1
#     reverse(left, right)

#     left, right = 0, len(nums) - 1
#     reverse(left, right)

#     return nums

# nums = [1,2,3,4,5]
# k = 6
# print(leftRotation(nums, k))

# -------------------------------------------------------------------------------------------

# def leftRotation(nums, k):
#     k %= len(nums)

#     def reverse(left, right):
#         while left < right:
#             nums[left], nums[right] = nums[right], nums[left]
#             left += 1
#             right -= 1

#     left, right = 0, k - 1
#     reverse(left, right)

#     left, right = k, len(nums) - 1
#     reverse(left, right)

#     left, right = 0, len(nums) - 1
#     reverse(left, right)

#     return nums

# nums = [1,2,3,4,5]
# k = 5
# print(leftRotation(nums, k))

# ---------------------------------------------------------------------------------------------














