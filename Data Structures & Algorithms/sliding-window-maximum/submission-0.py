class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []
        for lptr in range(len(nums)):
            fptr = lptr - k + 1
            heapq.heappush(heap, (-nums[lptr], lptr))
            if fptr >= 0:
                while heap[0][1] < fptr:
                    heapq.heappop(heap)
                result.append(-heap[0][0])
        return result