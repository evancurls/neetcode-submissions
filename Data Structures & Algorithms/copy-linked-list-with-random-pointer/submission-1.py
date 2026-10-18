"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #must have a hash map of seen values
        seen = {}
        if not head: return None
        rHead = Node(head.val, None, None)
        seen[head] = rHead
        base = head
        while head:
            rHead.val = head.val
            if head.next:
                if head.next not in seen:
                    temp = Node(head.next.val)
                    seen[head.next] = temp
                rHead.next = seen[head.next]
            if head.random:
                if head.random not in seen:
                    temp = Node(head.random.val)
                    seen[head.random] = temp
                rHead.random = seen[head.random]

            head = head.next
            rHead = rHead.next
        return seen[base]