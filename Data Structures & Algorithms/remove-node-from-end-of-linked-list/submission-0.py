# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #idea, reverse the list twice
        #n will always be less than or equal to sz, and there will always be at least 1 node in the list
        curNode = head
        prevNode = None

        i = 0
        while curNode:
            temp = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = temp
            i += 1
        
        print(i)
            
        #traverse list, reversing all heads
        print(prevNode.val)
        
        i = 1
        curNode = prevNode
        prevNode = None
        while curNode:
            print(f"Current Node: {curNode.val} with i: {i}")
            temp = curNode.next
            curNode.next = prevNode
            if i != n:
                prevNode = curNode
            curNode = temp
            i += 1
        
        return prevNode

        