class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle_index = (left + right) // 2
            if nums[middle_index] == target:
                return middle_index
            if nums[left] <= nums[middle_index]:
                if nums[left] <= target < nums[middle_index]:
                    right = middle_index - 1
                else:
                    left = middle_index + 1
            else:
                if nums[right] >=target > nums[middle_index]:
                    left = middle_index + 1
                else:
                    right = middle_index - 1
        return -1