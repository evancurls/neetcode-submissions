class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps = tempStack()
        newList = [0] * len(temperatures)
        
        for index, num in enumerate(temperatures):
            print(index)
            while not temps.isEmpty() and num > temps.peek():
                popIndex = temps.pop()
                newList[popIndex] = index - popIndex

            temps.push(num, index)
        return newList



class stackNode:
    def __init__(self, temp, index):
        self.temp = temp
        self.index = index
        self.next = None

class tempStack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, temp, index):
        newNode = stackNode(temp, index)

        if self.head:
            newNode.next = self.head
        self.head = newNode
        self.size += 1

    def pop(self):
        if self.isEmpty():
            return 0
        toRemove = self.head
        self.head = self.head.next
        self.size -= 1
        return toRemove.index

    def peek(self):
        if self.isEmpty():
            return 0
        return self.head.temp

    def isEmpty(self):
        return self.size == 0

    def stackSize(self):
        return self.size

        