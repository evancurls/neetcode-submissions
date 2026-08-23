# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #indexList = set()
        fastHead = head.next
        while fastHead:
            if fastHead.next == head or fastHead == head:
                return True
            fastHead = fastHead.next
            if fastHead:
                fastHead = fastHead.next
            head = head.next
        return False
        