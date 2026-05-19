class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numSeen = {}
        for num in nums:
            if num in numSeen:
                return num
            numSeen[num] = True