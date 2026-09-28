class TimeMap:
    def __init__(self):
        self.hash_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash_map:
            self.hash_map[key] = []
        self.hash_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash_map:
            return ""
        
        values = self.hash_map[key]
        if timestamp < values[0][0]:
            return ""

        left = 0
        right = len(values) - 1
        result = ""

        while left <= right:
            middle = (left + right) // 2
            middle_timestamp, middle_value = values[middle]
            
            if middle_timestamp <= timestamp:
                result = middle_value
                left = middle + 1  
            else:
                right = middle - 1

        return result
