class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        checkNums = set(nums)
        for num in checkNums:
            if num-1 not in checkNums:
                length = 1
                while num + length in checkNums:
                    length += 1
                longest = max(longest, length)

        return longest
        