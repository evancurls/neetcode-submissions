class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        largerNum = len(numbers) - 1
        for smallerNum in range(len(numbers)):
            while(numbers[smallerNum] + numbers[largerNum] > target):
                largerNum -= 1
            if(numbers[smallerNum] + numbers[largerNum] == target):
                return [smallerNum + 1,largerNum + 1]



        
        