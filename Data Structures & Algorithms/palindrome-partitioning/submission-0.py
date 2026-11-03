class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result, solution = [], []

        def backtracking(start):
            if start == len(s):
                result.append(solution[:])
                return
            for i in range(start, len(s)):
                substring = s[start:i + 1]

                if substring == substring[::-1]:
                    solution.append(substring)

                    backtracking( i + 1)
                    solution.pop()
        backtracking(0)
        return result

        