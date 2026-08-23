# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root)

    def traverse(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + max(self.traverse(root.left), self.traverse(root.right))
        