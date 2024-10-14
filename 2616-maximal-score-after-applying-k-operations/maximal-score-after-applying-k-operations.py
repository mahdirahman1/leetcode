class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        maxHeap = []
        for num in nums:
            heapq.heappush(maxHeap, -num)
        
        score = 0
        for _ in range(k):
            number = -heapq.heappop(maxHeap)
            score += number
            heapq.heappush(maxHeap, -math.ceil(number/3))
        
        return score