class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Sort on the basis of capital
        # Only add the projects in heap, whose capital can be affored.
        # MaxHeap on profit
        info = [list(item) for item in zip(profits, capital)]
        print(info)
        info.sort(key=lambda x: x[1])
        idx = 0
        heap = []
        n = len(capital)
        maxCap = w
        numP = 0
        while idx < n:
            while idx < n and info[idx][1] <= maxCap:
                heapq.heappush(heap, -info[idx][0])
                idx += 1
            if not heap:
                return maxCap
            profit = heapq.heappop(heap)
            maxCap += -profit
            numP += 1
            if numP == k:
                return maxCap
        while heap and numP < k:
            profit = heapq.heappop(heap)
            maxCap += -profit
            numP += 1
        return maxCap
