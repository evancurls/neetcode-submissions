class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        sums = []
        #unique combinations of nums where chosen sum to target
        def combination(summation, index, target):
            nonlocal sums
            #print(summation)
            if target < 0:
                return
            if nums[index] == target:
                newSum = summation + [nums[index]]
                #print(f"Adding newSum: {newSum}")
                sums.append(newSum)
            combination(
                summation + [nums[index]], 
                index, 
                target - nums[index])

            if index + 1 < len(nums):
                combination(
                    summation, 
                    index + 1, 
                    target)
            return
        combination([],0, target)
        return sums
                    
