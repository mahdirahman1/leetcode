class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(dict)
        for u, v, w in edges:
            graph[u][v] = w
            graph[v][u] = w

        def djikstra(graph, start):
            shortest_dist = defaultdict(int)
            # visited nodes
            visited = set()
            # pq 
            minHeap = [[0, start]]

            while minHeap:
                curr_dist, node = heapq.heappop(minHeap)
                
                if node in visited:
                    continue

                shortest_dist[node] = curr_dist
                visited.add(node)

                for n in graph[node]:
                    n_dist = graph[node][n]
                    if n not in shortest_dist or curr_dist + n_dist < shortest_dist[n]:
                        shortest_dist[n] = curr_dist + n_dist
                        heapq.heappush(minHeap, [shortest_dist[n], n])
            
            return shortest_dist
        
        distToLast = djikstra(graph, n)

        # dfs and find all paths from node 1
        visited = set()
        memo = defaultdict(int)
        def dfs(node):
            if node in visited:
                return memo[node]
            
            if node == n:
                return 1
            
            total = 0
            visited.add(node)
            for ne in graph[node]:
                if distToLast[ne] < distToLast[node]:
                    total += dfs(ne)

            memo[node] = total % (10**9 + 7)
            return memo[node]
        
        return dfs(1)