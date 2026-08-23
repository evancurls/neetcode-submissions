class Solution:

    OPERATIONS = {
        "+": lambda a, b: b + a,
        "-": lambda a, b: b - a, 
        "*": lambda a, b: b * a, 
        "/": lambda a, b: b / a,
    }

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        #need operations, to derive 
        for token in tokens:
            if token in self.OPERATIONS:
                opResult = self.OPERATIONS[token](int(stack.pop()), int(stack.pop()))
                stack.append(opResult)
            else:
                stack.append(token)
        
        return int(stack.pop())