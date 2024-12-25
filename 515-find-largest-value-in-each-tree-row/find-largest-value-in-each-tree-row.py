# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        largest_vals = []
        if not root:
            return []

        q = deque([root])
        while q:
            max_ = float("-inf")
            for _ in range(len(q)):
                node = q.popleft()
                max_ = max(max_, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            largest_vals.append(max_)
        
        return largest_vals