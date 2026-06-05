class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = 0
        q = deque()
        visit = set()
        adj = [set() for _ in range(n)]
        for edge in edges:      
            adj[edge[0]].add(edge[1])
            adj[edge[1]].add(edge[0])
        def bfs():
            nonlocal q
            nonlocal visit
            while q:
                node = q.popleft()
                for neigh in adj[node]:
                    if neigh not in visit:
                        visit.add(neigh)
                        q.append(neigh)

        for node in range(n):
            if node not in visit:
                res += 1
                q.append(node)
                visit.add(node)
                bfs()
        return res