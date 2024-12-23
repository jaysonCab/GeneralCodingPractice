class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        lowPosition = 0
        midPosition = 0
        highPosition = len(nums) - 1

        while midPosition <= highPosition:
            match nums[midPosition]:
                case 2:
                    nums[midPosition], nums[highPosition] = nums[highPosition], nums[midPosition]
                    highPosition -= 1
                case 0:
                    nums[midPosition], nums[lowPosition] = nums[lowPosition], nums[midPosition]
                    lowPosition += 1
                    midPosition += 1
                case 1:
                    midPosition += 1