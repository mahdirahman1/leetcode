class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            max_g = -heapq.heappop(gifts)
            heapq.heappush(gifts, -math.floor(sqrt(max_g)))
        
        return -sum(gifts)