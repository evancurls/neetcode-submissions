# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        curNode = root
        while curNode:
            if curNode == p or curNode == q:
                return curNode
            if curNode.val > p.val and curNode.val > q.val:
                curNode = curNode.left
                continue
            if curNode.val < p.val and curNode.val < q.val:
                curNode = curNode.right
                continue
            
            #print(f"{q.val} and {p.val} between {curNode.val}, returning curNode")
            return curNode
        return curNode
        