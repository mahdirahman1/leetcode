class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        right_max = [nums[-1]] * len(nums)
        for i in range(len(nums)-2, -1,-1):
            right_max[i] = max(nums[i], right_max[i+1])
        
        res = 0
        l = 0
        for r in range(1, len(nums)):
            left = nums[l]
            if left > right_max[r]:
                l += 1

            res = max(res, r-l)
           
        
        return res
