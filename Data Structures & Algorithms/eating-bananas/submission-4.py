import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left <= right:
            k = (left + right) // 2

            total_hours = 0

            for pile in piles:
                total_hours += math.ceil(pile / k)

            if total_hours <= h:
                right = k - 1
            else:
                left = k + 1

        return left