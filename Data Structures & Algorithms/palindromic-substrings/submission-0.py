class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = 0
        opt = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or opt[i+1][j-1]):
                    opt[i][j] = True
                    res += 1

        return res
