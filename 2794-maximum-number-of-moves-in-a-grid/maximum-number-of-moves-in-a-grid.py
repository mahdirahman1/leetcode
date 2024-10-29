class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        steps = [
            [1,1],
            [-1,1],
            [0,1]
        ]

        cache = defaultdict(int)

        def dfs(i,j, cache):
            if (i,j) in cache:
                return cache[(i,j)]
            
            res = 1
            neigh_max = 0
            for x,y in steps:
                new_i = i + x
                new_j = j + y
                if 0 <= new_i < len(grid) and 0 <= new_j < len(grid[0]) and grid[new_i][new_j] > grid[i][j]:
                    neigh_max = max(neigh_max, dfs(new_i, new_j, cache))
            
            cache[(i,j)] = 1 + neigh_max
            return cache[(i,j)]
        
        ans = 0
        for row in range(len(grid)):
            ans = max(ans, dfs(row, 0, cache) - 1)
        
        return ans