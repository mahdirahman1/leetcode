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

        nodes = set([node.val for node in nodes])
        self.ans = None
        def dfs(node, seen):
            if node is None:
                return seen
            
            left = dfs(node.left, set())
            right = dfs(node.right, set())

            all_seen = left.union(right)
            if node.val in nodes:
                all_seen.add(node.val)
            
            if all_seen == nodes:
                if self.ans is None:
                    self.ans = node
            
            return all_seen
                


          
        
        dfs(root, nodes)
        return self.ans