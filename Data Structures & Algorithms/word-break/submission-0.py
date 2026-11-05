class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        m = [False] * (len(s) + 1)
        m[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w) <= len(s)) and (s[i : i + len(w)] == w):
                    m[i] = m[i + len(w)]
                if m[i]:
                    break
        
        return m[0]