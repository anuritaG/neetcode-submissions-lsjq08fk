class Solution:
    def calPoints(self, operations: List[str]) -> int:
        scores = []
        for operation in operations:
            if operation == '+':
                a = int(scores[-1])
                b = int(scores[-2])
                scores.append(str(a+b))
            elif operation == 'C':
                scores.pop()
            elif operation == 'D':
                a = int(scores[-1])
                scores.append(str(a*2))
            else:
                scores.append(operation)
        res = 0
        for score in scores:
            res += int(score)
        return res
