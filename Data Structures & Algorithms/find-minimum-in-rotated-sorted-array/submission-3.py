class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            middle_index = (left + right) // 2
            if nums[middle_index] > nums[right]:
                left = middle_index + 1
            else:
                right = middle_index
        return nums[left]
