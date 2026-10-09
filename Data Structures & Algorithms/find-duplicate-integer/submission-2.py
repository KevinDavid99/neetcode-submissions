class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # numSeen = {}
        # for num in nums:
        #     if num in numSeen:
        #         return num
        #     numSeen[num] = True


        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if fast == slow:
                break
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow