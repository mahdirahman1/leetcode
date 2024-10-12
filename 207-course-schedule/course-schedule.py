class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = defaultdict(set)
        memo = set()
        for s,e in prerequisites:
            if s == e:
                return False

            graph[s].add(e)

        def dfs(node, visited, memo):
            if node in memo:
                return True

            if node in visited:
                return False
            
            visited.add(node)
            for n in graph[node]:
                if dfs(n, visited, memo) == False:
                    return False

            visited.remove(node)
            memo.add(node)
            return True
        
       

        for node in range(numCourses):
            visited = set()
            if node not in memo:
                if dfs(node, visited, memo) == False:
                    return False
            
        return True

       