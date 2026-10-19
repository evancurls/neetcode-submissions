class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = [[]]

        for num in nums:
            subsets += [ss + [num] for ss in subsets]
        return subsets