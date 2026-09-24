class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        num_of_rows = len(matrix)
        num_of_columns = len(matrix[0])
        total_num_of_element = num_of_rows * num_of_columns
        left = 0
        right = total_num_of_element - 1  

        while left <= right:
            middle_num = (left + right) // 2
            row_index = middle_num // num_of_columns
            column_index = middle_num % num_of_columns

            middle_num2 = matrix[row_index][column_index]

            if target == middle_num2:
                return True
            elif target < middle_num2:
                right = middle_num - 1
            else:
                left = middle_num + 1
        return False
        
