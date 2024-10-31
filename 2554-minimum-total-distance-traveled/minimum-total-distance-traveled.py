class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        m = len(robot)
        n = len(factory)
        
        dp = [inf] * m

        for j in range(n - 1, -1, -1): 
            prefix = 0 
            q = deque([(m, 0)])
            for i in range(m - 1, -1, -1): 
                prefix += abs(robot[i] - factory[j][0])
                if q[0][0] > i + factory[j][1]:
                    q.popleft()
                while q and q[-1][1] >= dp[i] - prefix:
                    q.pop()
                q.append((i, dp[i] - prefix))
                dp[i] = q[0][1] + prefix
        
        return dp[0]