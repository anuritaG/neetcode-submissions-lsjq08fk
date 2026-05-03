class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-i for i in stones]
        heapq.heapify(heap)
        while len(heap) > 1:
            print(heap)
            stone1 = -(heapq.heappop(heap))
            stone2 = -(heapq.heappop(heap))
            
            if stone1 > stone2:
                heapq.heappush(heap, -(stone1-stone2))
            else:
                heapq.heappush(heap, 0)
            
        return -heap[0]