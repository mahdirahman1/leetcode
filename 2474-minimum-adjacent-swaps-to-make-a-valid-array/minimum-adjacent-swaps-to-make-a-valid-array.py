class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        """
        loop and get index of max and min values
        two cases:
        1) if min index > max inded they will overlap when swapping
           total = min index swaps + max index swaps - 1 (will shift up by 1)
        2) if they dont overlap
            total = min index swaps + max index swaps
        """
        max_val, max_index = 0, -1
        min_val, min_index = float('inf'), -1
        for i, num in enumerate(nums):
            if num < min_val:
                min_val = num
                min_index = i
            
            if num >= max_val:
                max_val = num
                max_index = i
        
        total = min_index + (len(nums) - max_index - 1)
        if min_index > max_index:
            total -= 1
        
        return total
