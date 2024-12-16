class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        min_heap = []
        for i, num in enumerate(nums):
            heapq.heappush(min_heap, [num, i])
        
        for _ in range(k):
            num, idx = heapq.heappop(min_heap)
            nums[idx] = num * multiplier
            heapq.heappush(min_heap, [nums[idx], idx])
        
        return nums