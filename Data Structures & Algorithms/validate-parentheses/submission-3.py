class Solution:
    def isValid(self, s: str) -> bool:
        newStr = []
        meow = ["}",")","]"]
        meow2 = {"}":"{",")":"(","]":"["}
        for char in s:
            if char in meow2:
                if not newStr: return False
                temp = newStr.pop()
                print(temp)
                if temp != meow2[char]: return False
            else:
                newStr.append(char)
            print(newStr)
                
        print(newStr)
        return not newStr

    