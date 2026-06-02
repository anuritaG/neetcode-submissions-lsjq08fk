class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        nrows = len(grid)
        ncols = len(grid[0])
        def bfs(r, c):
            queue = deque()
            queue.append([r, c])
            grid[r][c] = 0
            area = 0
            while queue:
                curNode = queue.popleft()
                row = curNode[0]
                col = curNode[1]
                area += 1
                if row > 0 and grid[row-1][col] == 1:
                    queue.append([row-1, col])
                    grid[row-1][col] = 0
                if row < nrows - 1 and grid[row+1][col] == 1:
                    queue.append([row+1, col])
                    grid[row+1][col] = 0
                if col > 0 and grid[row][col-1] == 1:
                    queue.append([row, col-1])
                    grid[row][col-1] = 0
                if col < ncols - 1 and grid[row][col+1] == 1:
                    queue.append([row, col+1])
                    grid[row][col+1] = 0
            return area
        maxArea = 0
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    maxArea = max(maxArea, area)
        return maxArea