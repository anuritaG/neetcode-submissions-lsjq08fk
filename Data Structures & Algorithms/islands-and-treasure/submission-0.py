class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Multi source BFs, instead of starting from the land.
        # start BFS from the chest.
        # If we put all the treasues in the queue, before starting the BFS
        # the BFS from closest treasure reaches it first.
        nrows = len(grid)
        ncols = len(grid[0])
        visit = set()
        q = deque()
        def addCell(r, c):
            if r < 0 or r >= nrows or c < 0 or c >= ncols or grid[r][c] == -1:
                return
            if (r, c) in visit:
                return 
            q.append([r,c])
            visit.add((r,c))
        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visit.add((r,c ))
            
        dist = 0
        while q:
            # this is to ensure, the multi sourcing of BFS
            # basically, all the elements at same level are 
            # computed once. 
            # python computes len(q) before the loop starts.
            # but might need to be careful with other languages. 
            # compute len(q) before starting loop and store it
            for i in range(len(q)):
                node = q.popleft()
                r = node[0]
                c = node[1]
                grid[r][c] = dist
                addCell(r+1, c)
                addCell(r-1, c)
                addCell(r, c+1)
                addCell(r, c-1)
            dist += 1
        