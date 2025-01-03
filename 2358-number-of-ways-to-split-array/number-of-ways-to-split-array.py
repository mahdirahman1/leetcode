class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = []
        sum_ = 0
        for num in nums:
            sum_ += num
            prefix_sum.append(sum_)
        
        valid_splits = 0
        for i in range(len(nums)-1):
            if prefix_sum[i] >= prefix_sum[-1] - prefix_sum[i]:
                valid_splits += 1
        
        return valid_splits