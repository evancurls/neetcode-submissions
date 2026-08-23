class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxOutput = 0
        minPrice = 99999
        for num in prices:
            minPrice = min(num,minPrice)
            maxOutput = max(maxOutput, num - minPrice)
        
        return maxOutput