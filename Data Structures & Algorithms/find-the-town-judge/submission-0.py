class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # in adjacency list, the town judge should be present in the
        # outgoing edge list of every other node but no outgoing node from
        # itself.
        adjList = dict()
        for i in range(n):
            adjList[i+1] = []
        for rel in trust:
            adjList[rel[0]].append(rel[1])
        # no town judge, if multiple nodes have 0 outgoing edges
        count = 0
        potJudge = 0
        for node, edges in adjList.items():
            if len(edges) == 0:
                count += 1
                potJudge = node
        if count != 1:
            return -1
        for node, edges in adjList.items():
            if node != potJudge and potJudge not in edges:
                return -1
        return potJudge