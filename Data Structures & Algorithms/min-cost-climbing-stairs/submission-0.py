class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        print(n)
        print(cost)
        m = [-1] * (n + 1)
        print(m)
        #0 for both 0 and 1st step since we can start at either
        m[0],m[1],m[2] = 0, 0, min(cost[0],cost[1])

        for i in range(3, n+1):
            m[i] = min((m[i-1] + cost[i-1]), m[i-2] + cost[i-2])

        print(m)
        return m[n]
        