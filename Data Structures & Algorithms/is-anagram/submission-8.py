class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count, t_count = {}, {}
        
        for letter in range(len(s)):
            if s[letter] in s_count:
                s_count[s[letter]] +=1
            else:
                s_count[s[letter]] = 1
        
        for letter in range(len(t)):
            if t[letter] in t_count:
                t_count[t[letter]] +=1
            else:
                t_count[t[letter]] = 1
        
        return s_count == t_count