class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2: return n

        m = [-1] * (n + 1)
        m[1], m[2] = 1,2
        for i in range(3, n + 1):
            m[i] = m[i - 1] + m[i - 2]
        return m[n]

    #opt(n) = t(n-1) + t(n-2)
    #opt(0) = 0; opt(1) = 1; opt(2) = 2
    #for i in range(n):
    #    
        