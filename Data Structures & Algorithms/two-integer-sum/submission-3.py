class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        already_seen = {}

        for index, value in enumerate(nums):
            difference = target - value
            if difference in already_seen:
                return [already_seen[difference], index]
            else:
                already_seen[value] = index 
        return []
