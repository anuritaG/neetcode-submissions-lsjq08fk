class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Valid tree means there should be only one way to reach 
        # a particular node. If during BFS, we come across a cycle 
        #  --> no more a tree
        adjList = dict()
        for i in range(n):
            adjList[i] = []
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        visited = set()
        q = deque()
        print(adjList)
        visited.add(0)
        q.append([0, -1])
        while q:
            node, parent = q.popleft()
            print("node and parent", node, " ",parent)
            for neigh in adjList[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    q.append([neigh, node])
                else:
                    if neigh != parent:
                        print("faulty node", node, " ", parent, " ",neigh)
                        return False
        if len(visited) != n:
            print("here", visited)
            return False
        return True


