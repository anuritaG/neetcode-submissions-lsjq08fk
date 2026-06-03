class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # multi source BFS,
        nrows = len(grid)
        ncols = len(grid[0])
        visit = set()
        q = deque()
        fresh = 0
        def addCell(r, c):
            nonlocal fresh
            if r < 0 or r >= nrows or c < 0 or c >= ncols or (r,c) in visit:
                return
            if grid[r][c] != 1:
                return
            q.append([r,c])
            visit.add((r,c))
            fresh -= 1
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 2:
                    q.append([r,c])
                    visit.add((r,c))
                if grid[r][c] == 1:
                    fresh += 1
                 
        time = 0
        while fresh>0 and q:
            length = len(q)
            for i in range(length):
                node = q.popleft()
                r = node[0]
                c = node[1]
                addCell(r-1, c)
                addCell(r+1, c)
                addCell(r, c-1)
                addCell(r, c+1)
            time += 1
        print(time)
        if fresh > 0:
            return -1
        return time

            