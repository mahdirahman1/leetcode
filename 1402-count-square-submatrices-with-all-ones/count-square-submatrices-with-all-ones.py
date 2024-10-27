class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        cache = defaultdict(int)

        def dfs(i,j, cache):
            if (i,j) in cache:
                return cache[(i,j)]
                
            # return 0 for subproblems out of bounds
            if i >= len(matrix):
                return 0
            if j >= len(matrix[0]):
                return 0

            # if current value is 0, cant make subproblems so 0
            if matrix[i][j] == 0:
                cache[(i,j)] = 0
                return 0

            # solve the problem and subproblems from i,j
            # check three sides of i,j
            result = 1
            result += min(dfs(i+1,j, cache), dfs(i+1, j+1, cache), dfs(i, j+1, cache))
            
            cache[(i,j)] = result
            return result


        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                res += dfs(i,j, cache)

        return res
                

                
      