class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS = len(matrix)
        COLS = len(matrix[0])
        self.matrixSum = [[0 for _ in range(COLS+1)] for _ in range(ROWS+1)]

        for row in range(ROWS):
            prefix = 0
            for col in range(COLS):
                prefix = self.matrixSum[row + 1][col] +  self.matrixSum[row][col + 1]
                prefix = prefix + matrix[row][col] - self.matrixSum[row][col]
                self.matrixSum[row+1][col+1] = prefix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:

        result = self.matrixSum[row2+1][col2+1] - self.matrixSum[row1][col2+1] - self.matrixSum[row2+1][col1] + self.matrixSum[row1][col1]
        return result


      

        