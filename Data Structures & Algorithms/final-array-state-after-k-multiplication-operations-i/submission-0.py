class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []
        for i in range(len(nums)):
            heap.append((nums[i], i))
        heapq.heapify(heap)
        while k>0:
            l,i = heapq.heappop(heap)
            heapq.heappush(heap, (l*multiplier, i))
            k -= 1
        while heap:
            num, idx = heapq.heappop(heap)
            nums[idx] = num
        
        return nums