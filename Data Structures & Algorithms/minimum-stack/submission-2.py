class MinStack:

    def __init__(self):
        self.stack = []
        self.sortedStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not not self.sortedStack:
            val = min(self.sortedStack[-1],val)
        self.sortedStack.append(val)
        print(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.sortedStack.pop()

        

    def top(self) -> int:
        if not self.stack:
            return 0
        return self.stack[-1]

        

    def getMin(self) -> int:
        if not self.sortedStack:
            return 0
        return self.sortedStack[-1]
        
