class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        char_set = set()
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            size_of_window = (right - left) + 1
            max_length = max(max_length, size_of_window)
            char_set.add(s[right])
        return max_length

