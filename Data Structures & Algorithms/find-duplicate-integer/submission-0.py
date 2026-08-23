class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        checkDup = set()
        for num in nums:
            if num in checkDup:
                return num
            checkDup.add(num)
        return -1


        