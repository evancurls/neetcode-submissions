# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(n1, n2):
            if not n1 or not n2:
                if n1 or n2:
                    return False
                return True
            if n1.val != n2.val:
                return False
            
            return isIdentical(n1.left,n2.left) and isIdentical(n1.right, n2.right)

        def bfs(root, subroot):
            if not root or not subroot:
                if root or subroot:
                    return False
                return True
            if root.val == subroot.val:
                if isIdentical(root, subroot):
                    return True
            return bfs(root.left, subroot) or bfs(root.right,subroot)

        return bfs(root, subRoot)
                

                
        