class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result, solution = [],[]
        openParenthesis, closeParenthesis = 0,0

        def backtracking():
            nonlocal openParenthesis, closeParenthesis
            if openParenthesis == n and closeParenthesis == n:
                result.append(''.join(solution[:]))
                return
            if openParenthesis < n:
                solution.append("(")
                openParenthesis += 1

                backtracking()
                
                solution.pop()
                openParenthesis -= 1

            if closeParenthesis < openParenthesis:
                solution.append(")")
                closeParenthesis += 1

                backtracking()
                
                solution.pop()
                closeParenthesis -=1
        backtracking()
        return result
        
                
        