class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #two pass, sort by heights
        #or have a pointer at the end and beginning, compare sizes; moving forward whichever one is smaller
        l,r = 0, len(heights) - 1
        maxWater = 0
        print(r)
        while l < r:
            maxWater = max(maxWater, (r - l) * min(heights[l], heights[r]))
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxWater
        