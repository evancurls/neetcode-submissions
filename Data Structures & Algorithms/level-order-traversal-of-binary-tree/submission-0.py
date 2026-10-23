# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        retVal = []
        base = 0
        def bfs(node, base):
            nonlocal retVal
            if node is None:
                return

            #print(retVal)
            #print(f"Base level {base} for node {node.val} with list len: {len(retVal)}")
            #traversal
            if base > len(retVal) - 1:
                retVal.append([node.val])
            else:
                retVal[base].append(node.val)
            bfs(node.left, base + 1)
            bfs(node.right, base + 1)

        bfs(root, 0)
        return retVal

        