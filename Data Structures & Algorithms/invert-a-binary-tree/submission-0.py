# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #go to base, then up one. invert left and right. repeat for all the
        #print(f"Root: {root.val} Left: {root.left}")
        self.traverse(root) 
        return root

    def swapChildren(self, root: TreeNode):
        #print(f"{root.val}")
        temp = root.left
        root.left = root.right
        root.right = temp
    
    def traverse(self, root: TreeNode):
        if root:
            if root.left:
                print(f"{root.val}")
                self.traverse(root.left)
            if root.right:
                print(f"{root.val}")
                self.traverse(root.right)
            self.swapChildren(root)
        