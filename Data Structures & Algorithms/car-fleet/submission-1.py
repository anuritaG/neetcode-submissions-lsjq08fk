class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        carInfo = []
        for a, b in zip(position, speed):
            carInfo.append((a,b))
        carInfo.sort(key = lambda x:x[0], reverse=True)
        for carPos, carSpeed in carInfo:
            time = (target - carPos )/ carSpeed
            while len(stack) > 0 and time <= stack[-1]:
                time = stack[-1]
                stack.pop(-1)
            stack.append(time)
        return len(stack)