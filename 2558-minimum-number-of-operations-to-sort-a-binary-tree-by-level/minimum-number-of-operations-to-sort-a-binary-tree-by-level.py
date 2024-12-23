# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        swaps = 0
        q = deque([root])
        while q:
            index = 0
            index_map = defaultdict(int)
            arr = []
            for _ in range(len(q)):
                node = q.popleft()
                index_map[node.val] = index
                arr.append(node.val)
                index += 1
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            
            sorted_ = sorted(arr)
            for i in range(len(arr)):
                if arr[i] != sorted_[i]:
                    # find index of num at sorted_[i]
                    # set arr[i] = sorted_[i]
                    # set index of arr[i] as index of sorted_[i]
                    # set index of sorted_[i] as i
                    sort_index = index_map[sorted_[i]]
                    index_map[arr[i]] = sort_index
                    index_map[sorted_[i]] = i
                    arr[i], arr[sort_index] = arr[sort_index], arr[i]
                    swaps += 1

        return swaps
