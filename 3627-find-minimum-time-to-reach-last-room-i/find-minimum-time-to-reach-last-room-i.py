class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # djikstras algo, track shortest time to reach index (i,j)
        shortest_times = defaultdict(int)
        visited = set()
        
        steps = [
            [0,1],
            [0,-1],
            [1,0],
            [-1,0]
        ]

        #dist, index
        q = [(0, (0,0))]

        while q:
            curr_time, index = heapq.heappop(q)
            i,j = index

            if (i,j) in visited:
                continue

            visited.add((i,j))
            shortest_times[(i,j)] = curr_time

            for x,y in steps:
                new_i = x + i
                new_j = y + j
                if 0 <= new_i < len(moveTime) and 0 <= new_j < len(moveTime[0]):
                    new_time = curr_time
                    if moveTime[new_i][new_j] > curr_time:
                        new_time = moveTime[new_i][new_j]
                    heapq.heappush(q, [new_time + 1, (new_i, new_j)])


       
        return shortest_times[(len(moveTime)-1, len(moveTime[0])-1)]