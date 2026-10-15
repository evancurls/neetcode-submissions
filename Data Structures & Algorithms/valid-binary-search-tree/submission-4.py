# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        #idea, keep a window of least and greatest vals
        def valBST(node: Optional[TreeNode], min, max):
            if not node: return True
            if not min < node.val < max: return False

            return valBST(node.left, min=min, max=node.val) and valBST(node.right, min=node.val, max=max)
        
        return valBST(root, min=-1000000001, max=1000000001)
        