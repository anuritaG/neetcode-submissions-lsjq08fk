class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Incrementally built the heap. Store the tasks starting first.
        heap = []
        n = len(tasks)
        taskIndx = [(task[0], task[1], idx) for idx, task in enumerate(tasks)]
        taskIndx.sort(key = lambda x:x[0])
        idx = 0
        time = taskIndx[0][0]
        res = []
        while idx < n:
            # Push all tasks that can be started by that time
            while idx < n and taskIndx[idx][0] <= time:
                heapq.heappush(heap,[taskIndx[idx][1], taskIndx[idx][2]])
                idx += 1
            processedTask = heapq.heappop(heap)
            time = time + processedTask[0]
            res.append(processedTask[1])
            # If all tasks seen by now have been processed but next task 
            # can not be started yet, skip idle time.
            if idx < n and taskIndx[idx][0] > time and not heap:
                time = taskIndx[idx][0]
        while heap:
            processedTask = heapq.heappop(heap)
            res.append(processedTask[1])
        return res
