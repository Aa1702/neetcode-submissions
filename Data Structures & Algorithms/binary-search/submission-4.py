class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            median = (left + right)//2

            if nums[median] < target:
                left = median + 1

            elif nums[median] > target:
                right = median - 1

            elif nums[median] == target:
                return median
        return -1
