class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        setS = {}
        setT = {}

        if len(s) != len(t):
            return False

        for index in range(len(s)):
            setS[s[index]] = 1 + setS.get(s[index],0)
            setT[t[index]] = 1 + setT.get(t[index],0)


        return (setS == setT)