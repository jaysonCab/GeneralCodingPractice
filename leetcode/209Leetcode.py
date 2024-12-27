'''


INCOMPLETE



'''




# December 26th, 2024
# Damn time limit exceeded, couldn't complete

# class Solution:
#     def minSubArrayLen(self, target: int, nums: List[int]) -> int:
#         right = 0
#         minTotal = float('inf')
#         currentTotal = 0

#         for left in range(len(nums)):
#             if currentTotal >= target:
#                 minTotal = min(minTotal, right - left + 1)
            
#             right = left
#             currentTotal = 0
#             done = False
#             while not done:
#                 if currentTotal < target and right < len(nums):
#                     currentTotal += nums[right]
#                     right += 1
#                 else:
#                     done = True
        
#         if minTotal == float('inf'):
#             minTotal = 0

#         if currentTotal == target:
#             minTotal = min(minTotal, 1)

#         return minTotal

# ------------------------------------------------------------------------

# def minSubArrayLen(target, nums):
#     left = 0
#     right = 0
#     minTotal = float('inf')
#     total = 0

#     while left <= right:

#         if total < target:
#             total += nums[right]
#             right += 1
#         else:
#             minTotal = min(minTotal, right - left + 1)
#             total -= nums[left]
#             left += 1

#     return minTotal


# target = 7
# nums = [2,3,1,2,4,3]
# print(minSubArrayLen(target, nums))

# ----------------------------------------------------------------------------------------

def minSubArrayLen(target, nums):
    left = 0
    minTotal = float('inf')
    total = 0

    for right in range(len(nums)):
        total += nums[right]

        while total >= target:
            minTotal = min(minTotal, right - left + 1)
            total -= nums[left]
            left += 1

    if minTotal == float('inf'):
        return 0
    else:
        return minTotal

target = 7
nums = [2,3,1,2,4,3]
print(minSubArrayLen(target, nums))
 
# --------------------------------------------------------------------------------------

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        minTotal = float('inf')
        total = 0

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                minTotal = min(minTotal, right - left + 1)
                total -= nums[left]
                left += 1

        if minTotal == float('inf'):
            return 0
        else:
            return minTotal