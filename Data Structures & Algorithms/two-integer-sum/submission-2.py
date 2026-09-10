class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        already_seen_num = {}

        for index, value in enumerate(nums):
            diff_in_num = target - value
            if diff_in_num in already_seen_num:
                return [already_seen_num[diff_in_num], index]
            already_seen_num[value] = index
        return []


            
