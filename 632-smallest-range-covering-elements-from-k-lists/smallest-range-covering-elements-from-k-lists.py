class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        left = right = nums[0][0]
        
        k = len(nums)
        minHeap = []
        for i in range(k):
            l = nums[i]
            left = min(left, l[0])
            right = max(right, l[0])
            heapq.heappush(minHeap, [l[0], i, 0])
        
        
        res = [left, right]
    
        while True:
            _, li, index = heapq.heappop(minHeap)
            if index + 1 >= len(nums[li]):
                return res

            heapq.heappush(minHeap, [nums[li][index+1], li, index+1])

            left = minHeap[0][0]
            right = max(right, nums[li][index+1])
    

            if right-left < res[1]-res[0]:
                res = [left, right]
        
            
