# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(node, p, q):
            if node is None:
                return []

            descendants = []
            if node == p or node == q:
                descendants.append(node)
            
            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)

            if left and left[-1] == True:
                return left
            
            if right and right[-1] == True:
                return right

            descendants += left + right
            if len(descendants) == 2:
                return [node, True]

            return descendants

        res = dfs(root, p, q)

        if res[-1] == True:
            return res[0]
        
        return None
