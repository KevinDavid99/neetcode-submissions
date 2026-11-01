class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result, solution = [], []
        nums.sort()

        def backtrack(start):
            result.append(solution[:])
            for i in range(start, len(nums)):    
                if i > start and nums[i] == nums[i - 1]:
                    continue

                solution.append(nums[i])
                backtrack(i+1)
                solution.pop()

        backtrack(0)
        return result
