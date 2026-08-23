# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #two pointers likely
        #find length ig
        count = 0
        length = self.getSize(head) - 1
        left = head
        #print(f"Length: {length}")
        while left:
            right = left
            for i in range(length - 2):
                right = right.next
            #print(f"Left Node: {left.val} Right Node: {right.val} Length: {length}")
            #print("Before Swap:")
            #self.showList(head)
            right = self.pop(right)
            self.insert(left, right)
            left = left.next
            if left:
                left = left.next
            length -= 2
            #print("After Swap:")
            #self.showList(head)

    
    def getSize(self, head: ListNode) -> int:
        count = 1
        while head:
            #print(f"Node: {head.val} Count: {count}")
            head = head.next
            count += 1
        return count
        

    def showList(self, head: ListNode) -> None:
        newList = []
        while head:
            newList.append(head.val)
            head = head.next
        print(f"{newList}")
        return

    def insert(self, head: ListNode, replacement: ListNode) -> None:
        if replacement:
            temp = head.next
            head.next = replacement
            replacement.next = temp
        return

    def pop(self, head: ListNode) -> ListNode:
        if head.next:
            temp = head.next
            head.next = head.next.next
            temp.next = None
            return temp
        else:
            return None

        