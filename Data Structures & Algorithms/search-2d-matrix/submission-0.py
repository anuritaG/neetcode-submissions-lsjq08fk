class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # First search the row.
        # Then search the column
        low = 0
        high = len(matrix) - 1
        row = 0
        col = 0
        while low <= high:
            mid = (low + high) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                high = mid - 1
            else:
                low = mid + 1
        row = high
        low = 0 
        high = len(matrix[0]) - 1
        while low <= high:
            mid = (low + high) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
         
