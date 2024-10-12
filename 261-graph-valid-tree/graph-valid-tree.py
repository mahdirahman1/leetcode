class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # create a graph, find in_nodes of all nodes
        # if more than one node has an in_node of 0 return false
        # do a bfs starting from any node and look for cycle, use parent pointer to avoid child-parent cycle
        # all nodes must be connected

        graph = defaultdict(set)
        for s, e in edges:
            graph[s].add(e)
            graph[e].add(s)


        visited = set()
        q = deque([(0, None)])

        while q:
            for _ in range(len(q)):
                node, parent = q.popleft()
                visited.add(node)
                
                for nei in graph[node]:
                    if nei in visited and parent != None and nei != parent:
                        return False
                    
                    if nei != parent:
                        q.append((nei, node))

         
        if len(visited) != n:
            return False
        
        return True
