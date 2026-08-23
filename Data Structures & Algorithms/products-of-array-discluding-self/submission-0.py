class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newList = [0] * len(nums)
        product = 1
        product2 = 1
        for num in nums:
            if num == 0:
                product2 = product
            else:    
                product2 *= num
            product *= num
        for num in range(len(nums)):
            if nums[num] != 0:
                newList[num] = int(product / nums[num])
            else:
                newList[num] = product2
        return newList
        

        