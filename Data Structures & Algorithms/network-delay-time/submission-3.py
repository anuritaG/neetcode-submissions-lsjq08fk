class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Shortest Path Faster Update
        adj = [[] for _ in range(n+1)]
        for time in times:
            adj[time[0]].append((time[1], time[2]))
        q = deque()
        inQ = [False] * (n+1)
        dist = [float('inf')] * (n+1)
        q.append(k)
        inQ[k] = True
        dist[k] = 0
        while q:
            node = q.popleft()
            inQ[node] = False
            for neigh, curDist in adj[node]:
                newDist = min(dist[neigh], dist[node]+curDist)
                if newDist < dist[neigh]:
                    dist[neigh] = newDist
                    q.append(neigh)
                    inQ[neigh] = True
        res = max(dist[1:])
        if res == float('inf'):
            return -1
        return res