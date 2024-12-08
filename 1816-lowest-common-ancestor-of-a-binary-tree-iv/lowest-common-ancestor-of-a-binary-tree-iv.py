# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        """
        put nodes.val in a set
        do dfs and return lowest node when set is empty (all nodes are under this node)
        """

        seen = set(nodes)

        def dfs(root):
            if root in seen:
                return root

            if not root:
                return None

            left = dfs(root.left)
            right = dfs(root.right)

            if left and right:
                return root
            
            if left and not right:
                return left
        
            if right and not left:
                return right
            
            return None

        return dfs(root)