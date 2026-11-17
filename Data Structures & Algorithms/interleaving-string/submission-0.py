class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        m = {}

        def opt(i, j, k):
            # i is index in s1
            # j is index in s2
            # k is index in s3
            if k == len(s3):
                return (i == len(s1)) and (j == len(s2))
            if (i, j) in m:
                return m[(i,j)]
            
            res = False
            if i < len(s1) and s1[i] == s3[k]:
                res = opt(i + 1, j, k + 1)
            if not res and j < len(s2) and s2[j] == s3[k]:
                res = opt(i, j + 1, k + 1)
            
            m[(i,j)] = res
            return res
        return opt(0,0,0)

        