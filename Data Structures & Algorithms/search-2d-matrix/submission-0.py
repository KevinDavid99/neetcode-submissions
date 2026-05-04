class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1
        while left <= right:
            middle = (left + right) //2
            if target >= matrix[middle][0] and target <= matrix[middle][-1]:
                row = matrix[middle]

                left2 = 0
                right2 = len(row)-1
                while left2 <= right2:
                    middle2 = (left2 + right2) //2
                    if row[middle2] == target:
                        return True
                    elif row[middle2] < target:
                        left2 = middle2 + 1
                    else:
                        right2 = middle2 - 1
                return False
            elif target < matrix[middle][0]:
                right = middle - 1
            else:
                left = middle + 1

        return False
