class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        prevNum = 99999
        while left <= right:
            split = left + ((right - left) // 2)
            print(f"Split: {split}")
            prevNum = nums[split]
            if nums[split] == target:
                return split
            elif nums[split] > target:
                right = split - 1
            else:
                left = split + 1
        return -1
        