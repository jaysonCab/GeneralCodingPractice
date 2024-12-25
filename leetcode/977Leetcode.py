# December 24th, 2024
# Considered a two pointer, really cool

def squares(nums):
    left = 0
    right = len(nums) - 1
    newArray = []

    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

    while left <= right:
        if nums[right] >= nums[left]:
            newArray.append(nums[right])
            right -= 1
        else:
            newArray.append(nums[left])
            left += 1

    newArray.reverse()
    return newArray


nums = [-4,-1,0,3,10]
print(squares(nums))

# ---------------------------------------------------------------------------------------
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        left = 0
        right = len(nums) - 1
        newArray = []

        for i in range(len(nums)):
            nums[i] = nums[i] ** 2

        while left <= right:
            if nums[right] >= nums[left]:
                newArray.append(nums[right])
                right -= 1
            else:
                newArray.append(nums[left])
                left += 1

        newArray.reverse()
        return newArray
