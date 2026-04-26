class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Start from left -> right, check the gas balance at every step
        # If gas balance becomes -ve, we can not start from this station,
        # we reset the tank and try to start from the next station
        
        if sum(gas) < sum(cost):
            return -1 
        total = 0
        res = 0
        for i in range(len(gas)):
            total = total - cost[i] + gas[i]
            if total < 0:
                total = 0
                res = i + 1
        return res

        