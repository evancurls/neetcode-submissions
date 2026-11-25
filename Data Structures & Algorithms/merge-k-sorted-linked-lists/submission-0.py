# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        radix = Counter()
        ret_list = []
        for x_list in lists:
            while x_list:
                #print(x_list.val)
                radix[x_list.val] += 1
                x_list = x_list.next
            
        radix = sorted(radix.items())
        temp = ListNode(0,None)
        #print(radix)
        start = temp
        for key,value in radix:
            #print(f'looping {value} times for key {key}')
            for i in range(value):
                new_node = ListNode(key,None)
                ret_list.append(new_node)
                temp.next = new_node
                temp = new_node
        
        return start.next
            
        