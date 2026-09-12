class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            right_number = numbers[left] + numbers[right] 
            if right_number == target:
                return [left+1, right+1]
            elif right_number < target:
                left +=1
            else:
                right -=1
        return []
