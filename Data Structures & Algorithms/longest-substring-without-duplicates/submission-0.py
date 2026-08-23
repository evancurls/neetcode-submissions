class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ss = set()
        maxLen = 0
        l = 0

        for r in range(len(s)):
            #print(f"{s[c]}")
            while s[r] in ss:
                ss.remove(s[l])
                l += 1
            ss.add(s[r])
            maxLen = max(maxLen, r - l + 1)



        return maxLen


        