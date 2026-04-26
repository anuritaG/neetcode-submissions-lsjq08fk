class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = [0]*2
        for bill in bills:
            if bill == 5:
                change[0] += 1
            elif bill == 10:
                change[1] += 1
                change[0] -= 1
            else:
                if change[1] >= 1:
                    change[1] -= 1
                    change[0] -= 1
                else:
                    change[0] -= 3
            if change[0] < 0 or change[1] < 0:
                return False
        
        return True
        