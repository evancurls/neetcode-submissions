class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        maxFleet = 1

        #sort cars by position, also maintain speed
        sortedStack = sorted(list(zip(position, speed)), key=lambda x:x[0])
        arrivalTime = (target - sortedStack[-1][0]) / sortedStack[-1][1]

        for car in reversed(range(len(sortedStack))):
            newTime = (target - sortedStack[car][0]) / sortedStack[car][1]
            if newTime > arrivalTime:
                arrivalTime = newTime
                maxFleet += 1

        return maxFleet