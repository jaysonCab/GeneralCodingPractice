# December 19th, 2024
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        beginIndex = 0
        endIndex = len(nums) - 1

        while beginIndex <= endIndex:
            midpoint = beginIndex + (endIndex - beginIndex) // 2
            midpointValue = nums[midpoint]

            if midpointValue == target:
                return midpoint
            
            elif target < midpoint:
                endIndex = midpoint - 1

            else:
                beginIndex = midpoint + 1
        
        return None