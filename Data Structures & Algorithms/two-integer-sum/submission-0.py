class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seenNums = {}


        for index in range(len(nums)):
            #difference = 
            diff = target - nums[index]

            if diff in seenNums:
                return [seenNums[diff], index]

            seenNums[nums[index]] = index    
            

        