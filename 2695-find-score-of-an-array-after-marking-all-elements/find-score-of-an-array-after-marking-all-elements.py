class Solution:
    def findScore(self, nums: List[int]) -> int:
        min_heap = []
        for idx, num in enumerate(nums):
            heapq.heappush(min_heap, [num, idx])
        
        skipped = set()
        score = 0
        while min_heap:
            num, idx = heapq.heappop(min_heap)
            if idx in skipped:
                continue
            score += num
            skipped.add(idx+1)
            skipped.add(idx-1)
        
        return score
