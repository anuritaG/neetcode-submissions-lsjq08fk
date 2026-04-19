class Solution:
    def timeReq(self, piles, speed):
        time = 0
        for pile in piles:
            time += math.ceil(pile/speed)
        return time
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low + high) // 2
            print(mid, " ", self.timeReq(piles, mid))
            # if self.timeReq(piles, mid) == h:
            #     return mid
            if self.timeReq(piles, mid) > h:
                low = mid + 1
            else:
                high = mid - 1
        
        return low 
        