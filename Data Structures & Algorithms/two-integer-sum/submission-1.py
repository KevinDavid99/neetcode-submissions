class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dic = {}
        for i, v in enumerate(nums):
            difference = target - nums[i]
            if difference in my_dic:
                return [my_dic[difference], i]
        
            my_dic[v] = i