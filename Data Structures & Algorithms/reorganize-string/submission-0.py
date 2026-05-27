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
            # if len(res) == 0 or res[-1] != char:
            #     res += char
            #     freq = freq + 1
            #     if freq != 0:
            #         heapq.heappush(heap, [freq, char])
            # else:

                
        return res[1:]
