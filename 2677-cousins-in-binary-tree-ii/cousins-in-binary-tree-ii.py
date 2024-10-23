# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # pass 1, bfs or dfs and store total sum of each level
        # pass 2, dfs and set children value = level sum - sum of two/one children
        level_sum = defaultdict(int)

        def dfs(node, level, countLevels=True):
            if node is None:
                return

            if countLevels:
                level_sum[level] += node.val
            
            else:
                children_sum = 0
                children_sum += node.left.val if node.left else 0
                children_sum += node.right.val if node.right else 0
                if node.left:
                    node.left.val = level_sum[level+1] - children_sum
                if node.right:
                    node.right.val = level_sum[level+1] - children_sum
    
            dfs(node.left, level+1, countLevels)
            dfs(node.right, level+1, countLevels)
        
        dfs(root, 0)
        dfs(root, 0, False)
        root.val = 0
        return root