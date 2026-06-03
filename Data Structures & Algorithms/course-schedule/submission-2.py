class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # check for cycles
        # using topo sort for this : basically start with nodes having
        # 0 indeg, visit in neighbours and decrease their indegrees
        # if the neighbours have 0 indegree put them in queue
        # create adjacency list:
        adjList = dict()
        indeg = dict()
        for n in range(numCourses):
            indeg[n] = 0
            adjList[n] = []
        for pre in prerequisites:
            indeg[pre[0]] += 1
            adjList[pre[1]].append(pre[0])
        q = deque()
        visit = set()
        for node, deg in indeg.items():
            if indeg[node] == 0:
                visit.add(node)
                q.append(node)
        courses = 0
        while q:
            node= q.popleft()
            courses += 1
            for neigh in adjList[node]:
                indeg[neigh] -= 1
                if indeg[neigh] == 0:
                    visit.add(neigh)
                    q.append(neigh)
        return courses == numCourses
            
        