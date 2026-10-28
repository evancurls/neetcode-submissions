class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.backtrack([], nums, [False] * len(nums))
        return self.res
        #base case

        #list of lists
    def backtrack(self, perm, nums, pick):
        #base case finished permutation
        if len(perm) == len(nums):
            self.res.append(perm[:])
            return

        for i in range(len(nums)):  
            if not pick[i]:
                perm.append(nums[i])
                pick[i] = True
                #quick backtrack
                self.backtrack(perm,nums,pick)
                perm.pop()
                pick[i] = False      

        