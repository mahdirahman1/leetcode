class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
   
        for i in range(len(queries)):
            queries[i] = (queries[i], i)
        
        queries.sort()
        res = [0] * len(queries)

        prev_index = 0
        prev_max = 0
        for q, index in queries:
            max_ = prev_max
            curr = prev_index
            while curr < len(items) and items[curr][0] <= q:
                max_ = max(max_, items[curr][1])
                curr += 1
            prev_index = curr
            prev_max = max_
            res[index] = max_
        
        return res
