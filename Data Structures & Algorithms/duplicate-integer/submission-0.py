class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        element_seen = set()
        for n in nums:
            if n in element_seen:
                return True
            element_seen.add(n)
        return False
        