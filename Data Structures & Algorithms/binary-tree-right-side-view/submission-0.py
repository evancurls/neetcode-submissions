# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #postorder
        retVal = []

        def dfs(node, depth):
            if not node:
                return
            nonlocal retVal
            #print(f"Depth {depth} for Node: {node.val} and length: {len(retVal)}")
            if depth >= len(retVal):
                retVal.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)

        dfs(root, 0)
        return retVal
        