class TimeMap:

    def __init__(self):
        self.empty_hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.empty_hashmap:
            self.empty_hashmap[key] = []
        self.empty_hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.empty_hashmap:
            return ""
        left, right = 0, len(self.empty_hashmap[key]) - 1
        result = ''
        while left <= right:
            middle = (left + right) // 2
            middle_timestamp, middle_value = self.empty_hashmap[key][middle]
            if middle_timestamp <= timestamp:
                result = middle_value
                left = middle + 1
            else:
                right = middle - 1
        return result
