class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dup_seen = set()

        for num in nums:
            if num in dup_seen:
                return True
            dup_seen.add(num)
        return False
