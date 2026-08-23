class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charList = set(s)
        longestSet = 0
        
        for char in charList:
            count = 0
            print(f"{char}")
            l = 0
            for r in range(len(s)):
                if s[r] != char:
                    count += 1
                while count > k:
                    if s[l] != char:
                        count -= 1
                    l += 1
                longestSet = max(longestSet, r - l + 1)

        return longestSet
