class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        num_of_rows = len(matrix)
        num_of_columns = len(matrix[0])
        total_num_of_element = num_of_rows * num_of_columns
        left = 0
        right = total_num_of_element - 1  

        while left <= right:
            middle_index = (left + right) // 2
            row_index = middle_index // num_of_columns
            column_index = middle_index % num_of_columns

            current_num = matrix[row_index][column_index]

            if target == current_num:
                return True
            elif target < current_num:
                right = middle_index - 1
            else:
                left = middle_index + 1
        return False
        
