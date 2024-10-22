# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # bfs and add up sum in same level
        # keep a minHeap of size k
        minHeap = []

        q = deque([root])

        while q:
            level_sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                level_sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            if len(minHeap) < k:
                heapq.heappush(minHeap, level_sum)
            elif len(minHeap) == k and minHeap[0] < level_sum:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, level_sum)
        
        if len(minHeap) < k:
            return -1
        return minHeap[0]
            
