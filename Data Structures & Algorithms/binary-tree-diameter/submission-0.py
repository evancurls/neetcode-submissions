# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        leftHeight = self.maxLength(root.left)
        rightHeight = self.maxLength(root.right)

        other = max(self.diameterOfBinaryTree(root.left),
                    self.diameterOfBinaryTree(root.right))
        diameter = leftHeight + rightHeight
        return max(other,diameter)
        
    #diameter would equal the max length of the left side of the root plus the right side of the root,use a recursive algorithm for that potentially

    def maxLength(self, node: Optional[TreeNode]) -> int:
        print(node)
        if not node:
            return 0
        return 1 + max(self.maxLength(node.left), self.maxLength(node.right))