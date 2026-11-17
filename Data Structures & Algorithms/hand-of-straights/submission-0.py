class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        #two ideas:
        # sort list, have all numbers in a set w respect to num they occur
        # go through list in ascending order, if the number isnt == 0 
        # in the set, -= 1 that num and the next 4 numbers
        # if a num < 0 then return False
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        hand.sort()
        
        for num in hand:
            if count[num]:
                for i in range (num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1
        return True