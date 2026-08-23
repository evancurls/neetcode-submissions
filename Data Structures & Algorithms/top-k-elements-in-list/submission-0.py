class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        #makes length n buckets, including 0 and total length of list, validates both edges
        bucketList = [[] for i in range(len(nums) + 1)]


        for num in nums:
            numCount[num] = 1 + numCount.get(num,0)
        for num, quantity in numCount.items():
            bucketList[quantity].append(num)
        print(bucketList)

        retList = []
        for i in range(len(bucketList) - 1, 0, -1):
            for num in bucketList[i]:
                retList.append(num)
                if len(retList) == k:
                    return retList
        
        
