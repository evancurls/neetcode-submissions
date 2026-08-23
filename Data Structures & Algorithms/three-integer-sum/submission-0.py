class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        foundList = set()
        for i1, num1 in enumerate(nums):
            for i2, num2 in enumerate(nums):
                for i3, num3 in enumerate(nums):
                    if num1 + num2 + num3 == 0 and i1 != i2 and i2 != i3 and i3 != i1:
                        newList = [num1,num2,num3]
                        newList.sort()
                        foundList.add(tuple(newList))
        return list(foundList)


        