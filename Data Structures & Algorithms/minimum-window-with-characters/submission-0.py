class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count_t = {}
        count_window = {}
        need = len(set(t))
        have = 0
        result = ""
        result_length = float('inf')
        left = 0
        for ch in t:
            count_t[ch] = count_t.get(ch, 0) + 1
        for right in range(len(s)):
            count_window[s[right]] = count_window.get(s[right], 0) + 1
            if s[right] in count_t and count_window[s[right]] == count_t[s[right]]:
                have += 1
            while have == need:
                if right - left + 1 < result_length:
                    result_length = right - left + 1
                    result = s[left:right+1]

                count_window[s[left]] -= 1
                if s[left] in count_t and count_window[s[left]] < count_t[s[left]]:
                    have -= 1
                left += 1
        return result