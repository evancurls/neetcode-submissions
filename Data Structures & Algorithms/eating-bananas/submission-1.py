class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        bt = r

        while l <= r:
            k = (r + l) // 2
            time = 0
            #print(f"Current rate: {k} bananas")
            for b in piles:
                time += math.ceil(float(b) / k)
                #print(f"{b} bananas = {math.ceil(float(b) / k)} hours, total time = {time}")
            if time > h:
                l = k + 1
            else:
                bt = k
                r = k - 1
        return bt




