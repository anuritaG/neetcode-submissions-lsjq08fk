class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n =  len(heights[0])
       
        dist = [[float('inf') for _ in range(n)] for _ in range(m)]
        inQ = [[False for _ in range(n)] for _ in range(m)]
        q = deque()
        q.append([0,0])
        inQ[0][0] = True
        visit = set()
        # visit.add((0,0))
        dist[0][0] = 0
        print(dist)
        directions = [[-1,0], [1,0], [0,1], [0,-1]]
        # directions = [[1,0], [0,1]]
        i = 0
        while q:
            # i += 1
            # if i == 4:
            #     break
            r, c = q.popleft()
            inQ[r][c] = False
            # print(r, c)
            for dire in directions:
                    nc = c + dire[1]
                    nr = r + dire[0]
                    
                    if nr < 0 or nc < 0 or nr >= m or nc >= n:
                        continue
                    # print(nr," ", m , " ", nc, " ", n)
                    # print(dist[nr][nc])
                    newDist = max(dist[r][c], abs(heights[r][c] - heights[nr][nc]))
                    # print(nr, nc, newDist)
                    if newDist < dist[nr][nc]:
                        dist[nr][nc] = newDist
                        # print("current in Q", q)
                        # print(inQ)
                        if not inQ[nr][nc]:
                            q.append([nr,nc])
                            inQ[nr][nc] = True
        print(dist)
        return dist[m-1][n-1]
        return 0
            
