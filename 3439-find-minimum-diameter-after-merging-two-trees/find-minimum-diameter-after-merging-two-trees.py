class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        adjList_1 = defaultdict(set)
        for x,y in edges1:
            adjList_1[x].add(y)
            adjList_1[y].add(x)
        
        adjList_2 = defaultdict(set)
        for x,y in edges2:
            adjList_2[x].add(y)
            adjList_2[y].add(x)

        def getDiameter(adjList):
            self.diameter = 0
            def get_max_depth(node, visited):
                visited.add(node)
                max_d = []
                for n in adjList[node]:
                    if n not in visited:
                        # we want to keep two max in the heap
                        heapq.heappush(max_d, get_max_depth(n, visited))
                        if len(max_d) > 2:
                            heapq.heappop(max_d)

                # calculate and update max diameter here
                if not max_d:
                    return 0
                
                if len(max_d) == 1:
                    self.diameter = max(self.diameter, 1 + max_d[0])
                    return 1 + max_d[0]

                # 2 diameters in min heap
                self.diameter = max(self.diameter, 2 + max_d[0] + max_d[1])

                # return max of the two diameters
                return 1 + max_d[1]
            
            visited = set()
            get_max_depth(0, visited)
            return self.diameter
        
        d1 = getDiameter(adjList_1)
        d2 = getDiameter(adjList_2)
        
        """
        just find the diameter of both trees and ans would be max({d1,d2,(d1+1)/2 +(d2+1)/2+1)} as for minimum diameter you would always merge center point of both trees diameter. and diameter might not even change after merging if other tree is too small
        """

        return max(d1,d2, 1 + ceil(d1/2) + ceil(d2/2))