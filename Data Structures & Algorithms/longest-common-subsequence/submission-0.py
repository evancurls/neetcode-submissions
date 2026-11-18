class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = {}
        #opt(i,j) = max subsequence that can be created 
        #from text1[0:i] and text2[0:j]

        def opt(i,j):
            if i == len(text1) or j == len(text2):
                return 0
            if (i,j) in m:
                return m[(i,j)]
            if text1[i] == text2[j]:
                m[(i,j)] = 1 + opt(i+1,j+1)
                return m[(i,j)]
            else:
                m[(i,j)] = max(opt(i+1,j),opt(i,j+1))
                return m[(i,j)]
        
        return opt(0, 0)

        