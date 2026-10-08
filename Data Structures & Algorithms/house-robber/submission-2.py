class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        #memoize data
        m = [-1] * (n+1)
        if len(nums) <= 2:
            return max(nums)
        m[0], m[1] = nums[0], max(nums[0],nums[1])
        m[0], m[1],m[2] = nums[0],nums[1], max(nums[2] + nums[0], nums[1])
        for i in range(2, len(nums)):
            print(i)
            m[i] = max(m[i - 1], m[i-2] + nums[i],m[i-3] + nums[i])

        print(m)
        return m[len(nums) - 1]