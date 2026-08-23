class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        l1 = set()
        for num in nums:
            if num in l1:
                return True
            l1.add(num)
        return False