# December 24th, 2024

# def leet(nums, k):

#     if k == 1:
#         return nums[0]

#     maxAverage = 0.0
#     total = 0
#     for i in range(len(nums)-k+1):

#         for j in range(i,i+k):
#             total += nums[j]
        
#         average = float(total/k)
#         if average > maxAverage:
#             maxAverage = average
        
#         average = 0
#         total = 0

#     return maxAverage

# nums = [0,4,0,3,2]
# k = 1
# print(leet(nums, k))


# class Solution:
#     def findMaxAverage(self, nums: List[int], k: int) -> float:
#         if len(nums) == 1:
#             return nums[0]

#         maxAverage = float('-inf')
#         total = 0
#         for i in range(len(nums)-k+1):

#             for j in range(i,i+k):
#                 total += nums[j]
            
#             average = float(total/k)
#             if average > maxAverage:
#                 maxAverage = average
            
#             average = 0
#             total = 0
            
#         return maxAverage

# ------------------------------------------------------------------------------------------------

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total = 0

        for i in range(k):
            total += nums[i]

        maxAverage = total / k

        for i in range(k, len(nums)):
            total += nums[i]
            total -= nums[i-k]

            average = total / k
            maxAverage = max(average, maxAverage)

        return maxAverage
