class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        """
        build a graph from the edges
        do a dfs from 0 as root
        if left subtree divisble by k, exclude/split
        if right subtree divisible by k, exclude/split
        add current root (either by itself, curr + left, curr + right, curr + left + right)

        """
        adjList = defaultdict(set)
        for i in range(n):
            adjList[i] = set()
        
        for i,j in edges:
            adjList[i].add(j)
            adjList[j].add(i)
        
        visited = set()
        self.parts = 0
        def dfs(node, visited):
            visited.add(node)
            # if this is a leaf node, return its value
            if not adjList[node]:
                return values[node]
            
            total = values[node]
            for child in adjList[node]:
                if child not in visited:
                    res = dfs(child, visited)
                    if res % k == 0:
                        self.parts += 1
                    else:
                        total += res
            
            return total

        res = dfs(0, visited)
        if res % k == 0:
            self.parts += 1

        return self.parts

            