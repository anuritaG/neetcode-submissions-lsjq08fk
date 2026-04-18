class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # If there is a car c behind a car b with speed less than b, it will never catch up to it.
        # Only cars with speed >= b and behind b will form a fleet.
        # Sort by position and calc. time req,
        # For a car c, append to stack. Before appending check if there exists
        # and car in stack with time <= c, pop it 

        sorted_pair = sorted(zip(position, speed))
        fleet = []
        for position, speed in sorted_pair:
            time = (target - position)/ speed
            while fleet and fleet[-1] <= time:
                fleet.pop()
            fleet.append(time)
        return len(fleet)
