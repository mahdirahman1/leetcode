class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ans = -1
        for num in nums:
            longest = 0
            curr = num
            while curr in nums_set:
                longest += 1
                curr *= curr
            if longest > 1:
                ans = max(ans, longest)
        
        return ans

        