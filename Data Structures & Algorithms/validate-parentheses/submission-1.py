class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parens = {')':'(','}':'{',']':'['}

        for paren in s:
            if paren in parens:
                if not stack:
                    return False
                if stack.pop() != parens[paren]:
                    return False
            else:
                stack.append(paren)

        return not stack
        