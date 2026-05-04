class Solution:
    def isValid(self, s: str) -> bool:

        lookup_hash_map ={
            ")": "(", 
            "]": "[", 
            "}": "{",
        }


        stack = []
        for character in s:
            if character not in lookup_hash_map:
                stack.append(character)
            else:
                if not stack:
                    return False
                top = stack[-1]
                if top == lookup_hash_map[character]:
                    stack.pop()
                else:
                    return False
        return not stack


                
             
        