# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # dfs with root of both trees, if children values are opposite, swap them and continue
        # we will assume they are same if they are not opposte, this will be caught in base case below
        # base case, if node1.val != node2.val return False
        # base case, both are None = return True

        def dfs(node1, node2):
            if node1 is None and node2 is None:
                return True
            
            # one is missing
            if node1 is None or node2 is None:
                return False

            # value dont match
            if node1.val != node2.val:
                return False

            left = False
            right = False

            # check if children are opposite
            if node1.left and node2.left:
                if node1.left.val != node2.left.val:
                    # diff left values, keep node1, swap node2.left with node2.right
                    left = dfs(node1.left, node2.right)
                    right = dfs(node1.right, node2.left)
                else:
                    left = dfs(node1.left, node2.left)
                    right = dfs(node1.right, node2.right)

            elif node2.right and node1.right:
                if node1.right.val != node2.right.val:
                    # diff left values, keep node1, swap node2.left with node2.right
                    left = dfs(node1.left, node2.right)
                    right = dfs(node1.right, node2.left)
                else:
                    left = dfs(node1.left, node2.left)
                    right = dfs(node1.right, node2.right)
            else:
                # one of them or both are None, swap node2.left with node2.right and try
                left = dfs(node1.left, node2.right)
                right = dfs(node1.right, node2.left)

            return left and right

        return dfs(root1, root2)
            

            

        