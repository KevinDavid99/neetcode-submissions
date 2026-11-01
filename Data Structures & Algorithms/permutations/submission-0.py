class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer, solution = [], []
        
        def backtrack():
            if len(solution) == n:
                answer.append(solution[:])
                return

            for x in nums:
                if x not in solution:
                    solution.append(x)
                    backtrack()
                    solution.pop()
        backtrack()
        return answer