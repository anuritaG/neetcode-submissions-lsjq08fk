class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # A BFS on each island
        
        nrow = len(grid)
        ncol = len(grid[0])
        res = 0
        def bfs(r, c):
            queue = deque()
            queue.append([r,c ])
            grid[r][c] = '0'
            # global visited
            while queue:
                curNode = queue.popleft()
                row = curNode[0]
                col = curNode[1]
                if row > 0 and grid[row-1][col] == '1':
                    queue.append([row-1, col])
                    grid[row-1][col] = '0'
                if row < nrow - 1 and grid[row+1][col] == '1':
                    queue.append([row+1, col])
                    grid[row+1][col] = '0'
                if col > 0 and grid[row][col-1] == '1':
                    queue.append([row, col-1])
                    grid[row][col-1] = '0'
                if col < ncol - 1 and grid[row][col+1] == '1':
                    queue.append([row, col+1])
                    grid[row][col+1] = '0'
        for r in range(nrow):
            for c in range(ncol):
                if grid[r][c] == '1':
                    bfs(r, c)
                    res += 1
        return res

