class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        colSum = [[0 for _ in range(n)] for _ in range(m)]
        preSum = [[0 for _ in range(n)] for _ in range(m)]
        for col in range(n):
            for row in range(m):
                if row == 0:
                    colSum[row][col] = matrix[row][col]
                else:
                    colSum[row][col] = matrix[row][col] + colSum[row-1][col]
        for row in range(0, m):
            for col in range(0, n):
                if col == 0:
                    preSum[row][col] = colSum[row][col]
                else:
                    preSum[row][col] = colSum[row][col] + preSum[row][col-1]
              
        self.preSum = preSum
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        add = 0
        if row1 > 0 and col1 > 0:
            add = self.preSum[row1-1][col1-1]
        sub1 = 0
        if row1 > 0:
            sub1 = self.preSum[row1-1][col2]
        sub2 = 0
        if col1 > 0:
            sub2 = self.preSum[row2][col1-1]

        return self.preSum[row2][col2] - sub1 - sub2 + add


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)