class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        newString = s.lower()
        validChars = {'a','b','c','d','e','f','g','h','i',
                    'j','k','l','m','n','o','p','q','r','s',
                    't','u','v','w','x','y','z','0','1','2',
                    '3','4','5','6','7','8','9'}

        while(left <= right):
            while right > left and newString[right] not in validChars:
                right -= 1
            while left < right and newString[left] not in validChars:
                left += 1
            
            if(newString[left] != newString[right]):
                return False
            left += 1
            right -= 1

        return True

        