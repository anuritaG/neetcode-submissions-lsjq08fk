class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort the list
        people.sort(reverse=True)
        #Take 2 pointers
        n = len(people)
        lptr, rptr = 0, n - 1
        ans = 0
        while rptr > lptr:
            lperson = people[lptr]
            rperson = people[rptr]
            if lperson + rperson <= limit:
                rptr -= 1
            ans += 1
            lptr += 1 
        if lptr == rptr:
            ans += 1
        return ans 
        