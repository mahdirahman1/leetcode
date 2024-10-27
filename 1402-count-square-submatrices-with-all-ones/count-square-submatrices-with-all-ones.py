class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        res = 0
        for i in range(len(matrix)):
            sum_ = 0
            for j in range(len(matrix[0])):
                # count for 1x1
                if matrix[i][j]:
                    res += 1
                
                sum_ += matrix[i][j]
                matrix[i][j] = sum_

                # get the total ones for matrix ixj using prev sum in above row
                if i > 0:
                    matrix[i][j] += matrix[i-1][j]
        
        # now find all matrix from 2x2 onwards
        # highest square matrix size can be min(m, n) = nxn
        max_size = min(len(matrix), len(matrix[0]))

        for size in range(2, max_size+1):
            start = size-1
            for x in range(size-1, len(matrix)):
                for y in range(size-1, len(matrix[0])):
                    # find matrix using (x,y)
                    # if x - size exists, do matrix[x][y]-matrix[x-size][y]
                    # if y - size exists, do matrix[x][y] - matrix[x][y-size]
                    current = matrix[x][y]
                    if x-size >= 0:
                        current -= matrix[x-size][y]
                    if y-size >= 0:
                        current -= matrix[x][y-size]
                    
                    if x-size >=0 and y-size >= 0:
                        current += matrix[x-size][y-size]
                    
                    if current == size * size:
                        res += 1
        
        return res
            

