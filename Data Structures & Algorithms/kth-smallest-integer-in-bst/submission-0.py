# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        num_int = 0

        def dfs(node):
            nonlocal num_int
            if not node:
                return 0
            #left
            left_res = dfs(node.left)
            if left_res != 0:
                return left_res

            num_int += 1
            if num_int == k:
                return node.val
            if num_int > k:
                return 0
            
            return dfs(node.right)

        return dfs(root)
            


        