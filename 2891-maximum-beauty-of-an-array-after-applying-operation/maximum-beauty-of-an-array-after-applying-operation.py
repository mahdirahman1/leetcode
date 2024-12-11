class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        """
        use sliding window, find longest window
        where nums[j] - nums[i] <= 2*k where j > i
        """
        nums.sort()
        max_window = 0
        l = 0
        for r in range(len(nums)):
            while nums[r]-nums[l] > 2*k:
                l += 1
            
            max_window = max(max_window, r-l+1)
        
        return max_window
        