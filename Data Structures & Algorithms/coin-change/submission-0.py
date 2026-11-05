class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        m = [amount + 1] * (amount + 1)
        m[0] = 0

        for i in range(1,amount + 1):
            for c in coins:
                if i - c >= 0:
                    m[i] = min(m[i], 1 + m[i-c])
        
        if m[amount] != amount + 1:
            return m[amount]
        else:
            return -1