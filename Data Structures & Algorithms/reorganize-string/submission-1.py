class Solution:
    def reorganizeString(self, s: str) -> str:
        freqMap = {}
        for c in s:
            freqMap[c] = freqMap.get(c, 0) + 1
        heap = []
        for k,v in freqMap.items():
            heap.append([-v, k])
        print(freqMap)
        print(heap)
        heapq.heapify(heap)
        res = "0"
        while heap:
            fChar = heapq.heappop(heap)
            # If the last seen char matches the current one.
            # Pop the next most freq char, if no such char found, it 
            # is impossible to find a soln.
            if res[-1] == fChar[1]:
                notValidChar = fChar
                if not heap:
                    return ""
                fChar = heapq.heappop(heap)
                heapq.heappush(heap, notValidChar)
            freq, char = fChar
            res += char
            freq += 1
            if freq != 0:
                heapq.heappush(heap, [freq, char])
        return res[1:]
