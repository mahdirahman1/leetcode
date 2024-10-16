class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        if a:
            heapq.heappush(maxHeap, [-a, 'a'])
        if b:
            heapq.heappush(maxHeap, [-b, 'b'])
        if c:
            heapq.heappush(maxHeap, [-c, 'c'])

        res = []
        while maxHeap:
            max_count, char = heapq.heappop(maxHeap)

            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap:
                    break
                m1, char1 = heapq.heappop(maxHeap)
                res.append(char1)
                if m1 + 1 < 0:
                    heapq.heappush(maxHeap, [m1+1, char1])
            
            res.append(char)

            if max_count + 1 < 0:
                heapq.heappush(maxHeap, [max_count+1, char])
        
        print(res)

        return "".join(res)