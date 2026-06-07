class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        # Basically store each nodes in q, and then compute min distance 
        # to each surrounding node, 
        # store an inQ array to mark which node is currently in Q to avoid
        # time limit excedded.
        # Special care to add nodes to q only when the minAbs dist decreases
        # as it might lead to infinite loop otherwise, because of (-1,0) (1,0) directions
        m = len(heights)
        n =  len(heights[0])
        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        inQ = [[False for _ in range(n)] for _ in range(m)]
        q = deque()
        q.append([0,0])
        inQ[0][0] = True
        dist[0][0] = 0
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        while q:
            r, c = q.popleft()
            inQ[r][c] = False
            for dire in directions:
                    nc = c + dire[1]
                    nr = r + dire[0]
                    
                    if nr < 0 or nc < 0 or nr >= m or nc >= n:
                        continue
                    newDist = max(dist[r][c], abs(heights[r][c] - heights[nr][nc]))
                    if newDist < dist[nr][nc]:
                        dist[nr][nc] = newDist
                        if not inQ[nr][nc]:
                            q.append([nr,nc])
                            inQ[nr][nc] = True
        return dist[m-1][n-1]
        return 0
            
