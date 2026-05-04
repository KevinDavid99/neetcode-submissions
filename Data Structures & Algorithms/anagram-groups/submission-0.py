from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            data[key].append(s)
        return list(data.values())