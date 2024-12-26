# December 25th, 2024

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)

        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        left, right = 0, len(nums) - 1
        reverse(left, right)

        left, right = 0, k-1
        reverse(left, right)

        left, right = k, len(nums) - 1
        reverse(left, right) 

# ----------------------------------------------------------------------------------------------
