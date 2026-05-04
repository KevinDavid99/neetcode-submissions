class Solution:
    def topKFrequent(self, nums:List[int], k:int):
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        arrange = []
        for num, freq in count.items():
            arrange.append([freq, num])
        arrange.sort()

        result = []
        while len(result) < k:
            result.append(arrange.pop()[1])
        return result
        