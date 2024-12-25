# December 25th, 2024

def removeElement(nums, val):
    left = 0
    right = len(nums) - 1

    while left <= right:
        match nums[left]:
            case _ if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1

            case _:
                left += 1
    
    print(nums)
    return left

 
nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))

# -------------------------------------------------------------------------------------------
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            match nums[left]:
                case _ if nums[left] == val:
                    nums[left], nums[right] = nums[right], nums[left]
                    right -= 1

                case _:
                    left += 1
        
        return left