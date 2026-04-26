class Solution:
    def candy(self, ratings: List[int]) -> int:
        # Constraint 1: if we just consider just left neighbours, i.e. give more candies
        # if rating(i) > rating(i-1)
        # Constraint 2: if we consider just right neighbours, i.e. give more candies if
        # rating (i) > rating(i+1)
        # Min. candies req. to fulfil both constraints --> so take max and not sum
        # sum to be used  if each neighbour constraints give rewards
        n = len(ratings)
        leftArr, rightArr = [1]*n , [1]*n
        # leftArr[0] = 1
        for i in range(1,n):
            if ratings[i] > ratings[i-1]:
                leftArr[i] = leftArr[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                rightArr[i] = rightArr[i+1] + 1
        res = 0
        for i in range(n):
            res += max(leftArr[i], rightArr[i])
        return res