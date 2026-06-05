class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # Do a Topo sort and store the prereq courses for each node
        adjList = dict()
        preMap = [set() for _ in range(numCourses)]
        indeg = dict()
        for n in range(numCourses):
            adjList[n] = []
            indeg[n] = 0
        for p in prerequisites:
            adjList[p[0]].append(p[1])
            indeg[p[1]] += 1
        
        q = deque()
        # Find nodes without any incoming edges:
        for n in range(numCourses):
            if indeg[n] == 0:
                q.append(n)
        while q:
            node = q.popleft()
            for neigh in adjList[node]:
                # use a set to prevent the list from becoming huge
                preMap[neigh].update(preMap[node])
                preMap[neigh].add(node)
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    q.append(neigh)
        res = []
        for query in queries:
            if query[0] in preMap[query[1]]:
                res.append(True)
            else:
                res.append(False)
        return res
            
