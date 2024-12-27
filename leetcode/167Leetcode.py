class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        complete = []

        while left < right:
            if numbers[left] + numbers[right] == target:
                complete.append(left + 1)
                complete.append(right + 1)
                return complete

            elif numbers[left] + numbers[right] > target:
                right -= 1
            
            else:
                left += 1