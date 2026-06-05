class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Valid tree means there should be only one way to reach 
        # a particular node. If during BFS, we come across a cycle 
        #  --> no more a tree. 
        # How to check cycle in an undirected graph: store curNode 
        # and parent in q. If we come accross a node that is visited
        # but its parent is not same as the curNode, means there is 
        # a way of reaching the neigb through something else resulting
        # a cycle somewhere along the path that parent is also one of 
        # the ancestors of cur Node
        adjList = dict()
        for i in range(n):
            adjList[i] = []
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        visited = set()
        q = deque()
        visited.add(0)
        q.append([0, -1])
        while q:
            node, parent = q.popleft()
            for neigh in adjList[node]:
                if neigh not in visited:
                    visited.add(neigh)
                    q.append([neigh, node])
                else:
                    if neigh != parent:
                        return False
        if len(visited) != n:
            return False
        return True


