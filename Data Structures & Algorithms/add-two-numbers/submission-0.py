# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        pow10 = 1
        sum1 = 0
        while l1:
            sum1 += (l1.val * pow10)
            pow10 *= 10
            l1 = l1.next

        # print(sum1)
        sum2 = 0
        pow10 = 1
        while l2:
            sum2 += (l2.val * pow10)
            pow10 *= 10
            l2 = l2.next
        # print(sum2)
        s = sum1 + sum2
        print(s)
        pow10 = 1
        val = ((s % (pow10 * 10)) // pow10)
        # print(val)
        headNode = ListNode(val, None)
        temp1 = headNode
        pow10 *= 10
        while headNode:
            if pow10 <= s:
                val = ((s % (pow10 * 10)) // pow10)
                headNode.next = ListNode(val, None)
            headNode = headNode.next
            pow10 *= 10
        return temp1

        