class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #find the least value, then treat that as the start point of the array
        length = len(nums)
        l,r = 0, length - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m

        
        startpoint = l
        r = l + length - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m % length] == target:
                return m % length
            elif nums[m % length] > target:
                r = m - 1
            else:
                l = m + 1
        return -1
            

        