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
        # print("tasks", taskIndx)
        while idx < n:
            while idx < n and taskIndx[idx][0] <= time:
                # print("task", taskIndx[idx])
                heapq.heappush(heap,[taskIndx[idx][1], taskIndx[idx][2]])
                # print(heap)
                idx += 1
            # print("time", time, "heap", heap)
            processedTask = heapq.heappop(heap)
            # print("processed task", processedTask)
            time = time + processedTask[0]
            res.append(processedTask[1])
            # print("result",res, "new time", time)
            if idx < n and taskIndx[idx][0] > time and not heap:

                time = taskIndx[idx][0]
                # print("time changed here", time, "taskIndx[idx]", taskIndx[idx])
        # print("heap end", heap)
        while heap:
            processedTask = heapq.heappop(heap)
            # print("processed task", processedTask)
            res.append(processedTask[1])
            # print("res",res)
            

        return res
