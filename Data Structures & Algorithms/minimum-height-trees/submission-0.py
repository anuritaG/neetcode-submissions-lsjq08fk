class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Basically find the centroids (middle 2 nodes) in thw path.
        # Use a BFS, at each step, trim the leaves till atmost 2 nodes are left/
        adjList = [set() for _ in range(n)]
        if n == 1:
            return [0]
        deg = [0 for _ in range(n)]
        for edge in edges:
            adjList[edge[0]].add(edge[1])
            adjList[edge[1]].add(edge[0])
            deg[edge[0]] += 1
            deg[edge[1]] += 1
        
        # Leaves are those that have single edge in it.
        leaves = deque()
        # visit = set()
        for i in range(n):
            if deg[i] == 1:
                leaves.append(i)
                # visit.add(i)
        while leaves:
            if n <= 2:
                return list(leaves)
            # Cut out leaves at each level at the same time
            for _ in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for neigh in adjList[node]:
                    deg[neigh] -= 1
                    if deg[neigh] == 1:
                        leaves.append(neigh)
                    