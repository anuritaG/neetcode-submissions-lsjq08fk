class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #TopoSort
        adjList = dict()
        indeg = dict()
        for n in range(numCourses):
            adjList[n] = []
            indeg[n] = 0

        for pre in prerequisites:
            adjList[pre[1]].append(pre[0])
            indeg[pre[0]] += 1
        res = []
        q = deque()
        for n in range(numCourses):
            if indeg[n] == 0:
                q.append(n)
        courses = 0
        while q:
            node = q.popleft()
            res.append(node)
            courses += 1
            for neigh in adjList[node]:
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    q.append(neigh)
        if courses != numCourses:
            return []
        print(res)
        return res
        
    
     