class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result, solution = [], []
        n = len(nums)

        def backtrack(i, current_sum):
            if current_sum == target:
                result.append(solution[:])
                return

            if current_sum > target or i == n:
                return

            backtrack(i+1, current_sum)

            solution.append(nums[i])
            backtrack(i, current_sum + nums[i])
            solution.pop()
        backtrack(0,0)
        return result