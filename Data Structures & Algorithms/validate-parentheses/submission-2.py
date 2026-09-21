class Solution:
    def isValid(self, s: str) -> bool:

        lookup = {
            ")": "(", 
            "]": "[", 
            "}": "{",
        }

        stack = []

        for char in s:
            if char not in lookup:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != lookup[char]:
                    return False
        return not stack



                
             
        