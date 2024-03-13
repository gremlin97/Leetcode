class Solution:
    def pivotInteger(self, n: int) -> int:
        l = list(range(1, n+1))
        for i in range(n):
            # print(l, sum(l[0:i+1]), sum(l[i:len(l)+1]))
            if sum(l[0:i+1]) == sum(l[i:len(l)+1]):
                return (i + 1)
        return -1