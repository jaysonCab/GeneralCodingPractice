# December 21st, 2024, O(n)

# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
#         for i in range(len(nums)):
#             if target == nums[i] or target < nums[i]:
#                 return i
#         return len(nums)
    
# ---------------------------------------- I DIDN'T LEARN BINARY SEARCH FOR NO REASON

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            midpoint = left + (right - left) // 2
            midpointValue = nums[midpoint]

            if target == midpointValue:
                return midpoint

            elif target < midpointValue:
                right = midpoint - 1

            else:
                left = midpoint + 1
        
        return left
