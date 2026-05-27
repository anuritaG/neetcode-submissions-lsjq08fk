class MedianFinder:

    def __init__(self):
        self.fHeap = []
        self.lHeap = []

    def addNum(self, num: int) -> None:
        if not self.fHeap:
            heapq.heappush(self.fHeap, -num)
        else:
            if num <= -self.fHeap[0]:
                heapq.heappush(self.fHeap, -num)
            else:
                heapq.heappush(self.lHeap, num)

        # elif not self.lHeap:
        #     heapq.heappush(self.lHeap, num)
        # else: 
        #     if num >= self.lHeap[0]:
        #         heapq.heappush(self.lHeap, num)
        #     else:
        #         heapq.heappush(self.fHeap, -num)
        if len(self.fHeap) > len(self.lHeap)+1:
            moveNum = heapq.heappop(self.fHeap)
            heapq.heappush(self.lHeap, -moveNum)
        if len(self.lHeap) > len(self.fHeap) + 1:
            moveNum = heapq.heappop(self.lHeap)
            heapq.heappush(self.fHeap, -moveNum)

    def findMedian(self) -> float:
        print("first half", self.fHeap)
        print("second half", self.lHeap)
        if (len(self.fHeap) + len(self.lHeap)) % 2 == 0:
           return (-self.fHeap[0] + self.lHeap[0])/ 2
        else:
            if len(self.fHeap) > len(self.lHeap):
                return -self.fHeap[0]
            return self.lHeap[0]
            
        
        