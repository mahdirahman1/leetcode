class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remainder = total % p
        prefix_map = defaultdict(int)
        prefix_map[0] = -1

        if remainder == 0:
            return 0
        
        res = len(nums)
        prefix_sum = 0
        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            prefix = (prefix_sum - remainder + p) % p
            if prefix in prefix_map:
                res = min(res, i - prefix_map[prefix])
            
            prefix_map[prefix_sum] = i

        if res == len(nums):
            return -1
        
        return res