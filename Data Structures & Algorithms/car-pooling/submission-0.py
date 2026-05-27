class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # Line Sweep Algo.
        tripMap = dict()
        # dropMap = dict()
        for trip in trips:
            psngr, startP, dropP = trip
            tripMap[startP] = tripMap.get(startP, 0) + psngr
            tripMap[dropP] = tripMap.get(dropP, 0) - psngr
        
            # dropMap[dropP] = dropMap[dropP] - psngr
        tripMapSorted = dict(sorted(tripMap.items()))
        print(tripMapSorted)
        curCap = 0
        for loc, num in tripMapSorted.items():
            curCap += num
            if curCap > capacity:
                return False
            curCap = max(curCap, 0)
        return True
        