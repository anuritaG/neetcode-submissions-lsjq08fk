class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x = point[0]
            y = point[1]
            distance = (x*x)+(y*y)
            heapq.heappush(heap, [-distance, x, y])
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for points in heap:
            res.append([points[1], points[2]])
        return res